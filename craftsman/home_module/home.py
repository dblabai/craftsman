import asyncio
import ctypes
import os
import platform
from shlex import quote
import shlex
import shutil
import subprocess
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QApplication
from PySide6.QtCore import Qt, Slot, QUrl
from PySide6.QtGui import QIcon, QDesktopServices

from craftsman.core.app_support_path import (
    app_compile_path,
    pip_env_path,
    python_env_path,
)
from craftsman.core.constants import SystemConstants
from craftsman.core.init_app import init_env
from craftsman.utils.compile_worker import CompileWorker
from craftsman.utils.cmtf_util import read_config_file, write_config_file
from craftsman.utils.convert_util import (
    convert_to_args,
    convert_to_include_data_dir_args,
)
from craftsman.utils.file_util import (
    find_first_file_with_pattern,
    match_file,
    match_files_with_extensions,
    open_select_file,
    open_select_folder,
)
from craftsman.ui.home_ui import Ui_MainWindow
from craftsman.utils.message_util import show_message


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        init_env()

        self.platform_system = platform.system()
        if self.platform_system == "Windows":
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                SystemConstants.APP_NAME
            )

        self.compile_worker = None

        self.m_ui = Ui_MainWindow()
        self.m_ui.setupUi(self)

        self.init_view()

    def init_view(self):
        self.m_ui.actionCompile.setEnabled(True)
        for item in ["Release", "Beta", "RC", "Preview"]:
            self.m_ui.versionTypeComboBox.addItem(item)
        self.m_ui.logPlainTextEdit.setReadOnly(True)

        self.new_cmtf()

        self.m_ui.iconPushButton.clicked.connect(self.pick_icon)
        self.m_ui.mainCodePushButton.clicked.connect(self.pick_main_code)
        self.m_ui.requirementsPushButton.clicked.connect(self.pick_requirements)
        self.m_ui.sourceFolderPushButton.clicked.connect(self.pick_source_folder)
        self.m_ui.sourceFilePushButton.clicked.connect(self.pick_source_file)
        self.m_ui.sourceRemovePushButton.clicked.connect(self.remove_source)
        self.m_ui.beforeScriptPushButton.clicked.connect(self.pick_before_script)
        self.m_ui.afterScriptPushButton.clicked.connect(self.pick_after_script)
        self.m_ui.outputPathPushButton.clicked.connect(self.pick_output_folder)

        self.m_ui.actionNew.triggered.connect(self.new_cmtf)
        self.m_ui.actionOpen.triggered.connect(self.open_cmtf)
        self.m_ui.actionSave.triggered.connect(lambda: self.compile_app(False))
        self.m_ui.actionCompile.triggered.connect(lambda: self.compile_app(True))
        self.m_ui.actionHelp.triggered.connect(
            lambda: QDesktopServices.openUrl(
                QUrl("https://github.com/dblabai/craftsman")
            )
        )

    def show_version(self):
        nuitka_command = f"{python_env_path()} -m nuitka --version"
        result = subprocess.run(
            nuitka_command, shell=True, capture_output=True, text=True
        )

        if result.returncode == 0:
            self.m_ui.logPlainTextEdit.setPlainText(result.stdout)
        else:
            self.m_ui.logPlainTextEdit.setPlainText("Error running ls command.")

    @Slot()
    def pick_icon(self):
        self.m_ui.iconLineEdit.setText(
            open_select_file(
                self.m_ui.iconLineEdit.text(), "Image Files (*.png *.ico *.icns)"
            )
        )

    @Slot()
    def pick_main_code(self):
        self.m_ui.mainCodeLineEdit.setText(
            open_select_file(self.m_ui.mainCodeLineEdit.text(), "Python Files (*.py)")
        )

    @Slot()
    def pick_requirements(self):
        self.m_ui.requirementsLineEdit.setText(
            open_select_file(
                self.m_ui.requirementsLineEdit.text(), "Requirements Files (*.txt)"
            )
        )

    @Slot()
    def pick_source_folder(self):
        folder_path = open_select_folder()
        self.add_source(folder_path, "folder")
        if not self.m_ui.mainCodeLineEdit.text():
            main_path = find_first_file_with_pattern(folder_path, r"(main|app)")
            self.m_ui.mainCodeLineEdit.setText(main_path)
        if not self.m_ui.requirementsLineEdit.text():
            requirements_path = match_file(folder_path, "requirements.txt")
            self.m_ui.requirementsLineEdit.setText(requirements_path)
        if not self.m_ui.iconLineEdit.text():
            icon_path = match_files_with_extensions(folder_path, (".png", ".ico"))
            self.m_ui.iconLineEdit.setText(icon_path)
        if not self.m_ui.outputPathLineEdit.text():
            self.m_ui.outputPathLineEdit.setText(os.path.join(folder_path, "output"))

    @Slot()
    def pick_source_file(self):
        file_path = open_select_file(self.m_ui.mainCodeLineEdit.text(), "All Files (*)")
        self.add_source(file_path, "file")

    @Slot()
    def pick_before_script(self):
        self.m_ui.beforeScriptLineEdit.setText(
            open_select_file(
                self.m_ui.beforeScriptLineEdit.text(), "Python Files (*.py)"
            )
        )

    @Slot()
    def pick_after_script(self):
        self.m_ui.afterScriptLineEdit.setText(
            open_select_file(
                self.m_ui.afterScriptLineEdit.text(), "Python Files (*.py)"
            )
        )

    def add_source(self, source_path, path_type):
        if source_path:
            item = QListWidgetItem(source_path)
            item.setData(Qt.UserRole, path_type)
            if path_type == "file":
                icon = QIcon(":/resources/icon/document_text.png")
            else:
                icon = QIcon(":/resources/icon/folder.png")
            item.setIcon(icon)
            self.m_ui.sourceFilesListWidget.addItem(item)

    @Slot()
    def pick_output_folder(self):
        self.m_ui.outputPathLineEdit.setText(
            open_select_folder(self.m_ui.outputPathLineEdit.text())
        )

    @Slot()
    def remove_source(self):
        for item in self.m_ui.sourceFilesListWidget.selectedItems():
            self.m_ui.sourceFilesListWidget.takeItem(
                self.m_ui.sourceFilesListWidget.row(item)
            )

    @Slot(bool)
    def compile_app(self, is_compile: bool):
        self.m_ui.actionCompile.setEnabled(False)

        app_name = self.m_ui.nameLineEdit.text()
        if not app_name:
            show_message(self.tr("Please enter Name"))
            self.m_ui.actionCompile.setEnabled(True)
            return

        app_format = ".exe" if self.platform_system == "Windows" else ""

        version_text = self.m_ui.versionLineEdit.text()
        version_increase = self.m_ui.versionIncreaseCheckBox.isChecked()
        version_type = self.m_ui.versionTypeComboBox.currentText()
        show_version_type = self.m_ui.showVersionTypeCheckBox.isChecked()

        app_pack_name = f"{app_name}{version_text}"
        if show_version_type:
            app_pack_name += f"-{version_type}"

        compile_path = app_compile_path(app_pack_name)

        compile_mode = self.m_ui.compileModeComboBox.currentText()
        console_current_index = self.m_ui.consoleComboBox.currentIndex()
        if self.platform_system == "Windows":
            console_current = (
                "--windows-disable-console" if console_current_index == 1 else ""
            )
        else:
            console_current = ""

        app_icon = self.m_ui.iconLineEdit.text()
        if app_icon:
            if self.platform_system == "Windows":
                app_icon = f"--windows-icon-from-ico={quote(app_icon)}"
            elif self.platform_system == "Darwin":
                app_icon = f"--macos-app-icon={quote(app_icon)}"
            else:
                app_icon = ""

        main_code = self.m_ui.mainCodeLineEdit.text()
        if not main_code:
            show_message(self.tr("Please select the main code file"))
            self.m_ui.actionCompile.setEnabled(True)
            return
        else:
            if is_compile:
                shutil.copy(main_code, compile_path)

        requirements = self.m_ui.requirementsLineEdit.text()

        # copy code 正在复制文件到虚拟环境中
        if is_compile:
            self.show_log_message(self.tr("Copying files to virtual environment"))

        source_files = []
        for index in range(self.m_ui.sourceFilesListWidget.count()):
            item = self.m_ui.sourceFilesListWidget.item(index)
            source_path = item.text()
            path_type = item.data(Qt.UserRole)
            source_files.append({"sourcePath": source_path, "sourceType": path_type})
            if is_compile:
                if path_type == "file":
                    shutil.copy(source_path, compile_path)
                else:
                    shutil.copytree(source_path, compile_path, dirs_exist_ok=True)

        enable_plugin = self.m_ui.enablePluginLineEdit.text()
        include_package = self.m_ui.includePackageLineEdit.text()
        include_data_dir = self.m_ui.includeDataDirLineEdit.text()

        before_script = self.m_ui.beforeScriptLineEdit.text()
        after_script = self.m_ui.afterScriptLineEdit.text()
        output_path = self.m_ui.outputPathLineEdit.text()
        if not output_path:
            show_message(self.tr("Please select application output path"))
            self.m_ui.actionCompile.setEnabled(True)
            return

        remove_output = self.m_ui.removeOutputCheckBox.isChecked()
        remove_output_command = "--remove-output" if remove_output else ""

        cm_config = {
            "appName": app_name,
            "version": version_text,
            "versionIncrease": version_increase,
            "versionType": version_type,
            "showVersionType": show_version_type,
            "system": self.m_ui.systemLineEdit.text(),
            "compileMode": compile_mode,
            "consoleWindows": self.m_ui.consoleComboBox.currentText(),
            "icon": self.m_ui.iconLineEdit.text(),
            "mainCode": main_code,
            "requirements": requirements,
            "sourceFiles": source_files,
            "enablePlugin": enable_plugin,
            "includePackage": include_package,
            "includeDataDir": include_data_dir,
            "beforeScript": before_script,
            "afterScript": after_script,
            "outputPath": output_path,
            "removeOutput": remove_output,
        }
        write_config_file(cm_config, os.path.join(output_path, f"{app_name}.cmtf"))
        self.show_log_message(self.tr("Saved successfully."))

        if not is_compile:
            self.m_ui.actionCompile.setEnabled(True)
            return

        # 正在准备编译应用程序
        self.show_log_message(self.tr("Prepare to compile the application"))

        if before_script:
            # 正在执行编译应用程序前置脚本
            self.show_log_message(
                self.tr("Executing script before compiling application")
            )
            before_command = f"{quote(python_env_path())} {quote(before_script)}"
            self.run_command(before_command, compile_path)

        if requirements:
            # 正在安装依赖
            self.show_log_message(self.tr("Installing dependency packages"))
            requirements_command = (
                f"{quote(pip_env_path())} install -r {quote(requirements)}"
            )
            self.run_command(requirements_command, compile_path)

        mac_command = ""
        if self.platform_system == "Darwin":
            mac_command = "--macos-create-app-bundle"
            if compile_mode == "standalone":
                mac_command += f" --macos-app-name={app_pack_name}"

        nuitka_command = f"""
            {quote(python_env_path())} -m nuitka \
            --{compile_mode} \
            {console_current} \
            {convert_to_args("--enable-plugin={}",enable_plugin)} \
            {convert_to_args("--include-package={}",include_package)} \
            {convert_to_include_data_dir_args(include_data_dir)} \
            --output-dir={quote(output_path)} \
            -o {quote(app_pack_name)}{app_format} \
            {app_icon} \
            {mac_command} \
            {remove_output_command} \
            {quote(main_code)}
        """
        # 正在编译应用
        self.show_log_message(self.tr("Compiling application"))
        self.show_log_message(nuitka_command)
        self.compile_worker = CompileWorker()
        self.compile_worker.stdout.connect(self.show_log_message)
        self.compile_worker.finished.connect(
            lambda: self.nuitka_finished(
                after_script, compile_path, app_pack_name, output_path
            )
        )
        asyncio.ensure_future(self.compile_worker.start(nuitka_command, compile_path))

    def nuitka_finished(self, after_script, compile_path, app_pack_name, output_path):
        if self.platform_system == "Darwin":
            old_app_path = f"{output_path}/main.app"
            if os.path.exists(old_app_path):
                try:
                    os.rename(old_app_path, f"{output_path}/{app_pack_name}.app")
                except Exception as e:
                    # 重命名应用时发生错误
                    show_message(
                        self.tr(f"An error occurred while renaming the app: {str(e)}")
                    )

        if after_script:
            # 正在执行编译应用程序后置脚本
            self.show_log_message(self.tr("Executing compile application post-script"))
            after_command = f"{quote(python_env_path())} {quote(after_script)}"
            self.run_command(after_command, compile_path)

        self.m_ui.actionCompile.setEnabled(True)
        show_message(self.tr("Application packaging completed."))

    @Slot()
    def new_cmtf(self):
        self.m_ui.nameLineEdit.setText("")
        self.m_ui.versionLineEdit.setText(f"-v1.0")
        self.m_ui.versionTypeComboBox.setCurrentIndex(0)
        self.m_ui.systemLineEdit.setText(f"{self.platform_system} {platform.release()}")
        self.m_ui.compileModeComboBox.setCurrentIndex(0)
        self.m_ui.consoleComboBox.setCurrentIndex(0)
        self.m_ui.sourceFilesListWidget.clear()
        self.m_ui.mainCodeLineEdit.setText("")
        self.m_ui.requirementsLineEdit.setText("")
        self.m_ui.iconLineEdit.setText("")
        self.m_ui.enablePluginLineEdit.setText("")
        self.m_ui.includePackageLineEdit.setText("")
        self.m_ui.includeDataDirLineEdit.setText("")
        self.m_ui.beforeScriptLineEdit.setText("")
        self.m_ui.afterScriptLineEdit.setText("")
        self.m_ui.outputPathLineEdit.setText("")
        self.m_ui.removeOutputCheckBox.setChecked(True)
        self.m_ui.logPlainTextEdit.clear()

    @Slot()
    def open_cmtf(self):
        file_path = open_select_file("", "Craftsman Files (*.cmtf)")
        if file_path:
            cmtf_data = read_config_file(file_path)
            self.m_ui.nameLineEdit.setText(cmtf_data.get("appName"))
            version_text = cmtf_data.get("version")
            version_increase = cmtf_data.get("versionIncrease")
            if version_increase:
                version = version_text.split(".")
                main_versions = ".".join(version[:-1])
                patch_version = str(int(version[-1]) + 1)
                version_text = f"{main_versions}.{patch_version}"

            self.m_ui.versionLineEdit.setText(version_text)
            self.m_ui.versionIncreaseCheckBox.setChecked(version_increase)
            self.m_ui.versionTypeComboBox.setCurrentText(cmtf_data.get("versionType"))
            self.m_ui.showVersionTypeCheckBox.setChecked(
                cmtf_data.get("showVersionType")
            )
            self.m_ui.compileModeComboBox.setCurrentText(cmtf_data.get("compileMode"))
            self.m_ui.consoleComboBox.setCurrentText(cmtf_data.get("consoleWindows"))
            self.m_ui.iconLineEdit.setText(cmtf_data.get("icon"))
            self.m_ui.mainCodeLineEdit.setText(cmtf_data.get("mainCode"))
            self.m_ui.requirementsLineEdit.setText(cmtf_data.get("requirements"))
            for source_file in cmtf_data.get("sourceFiles"):
                self.add_source(
                    source_file.get("sourcePath"), source_file.get("sourceType")
                )
            self.m_ui.enablePluginLineEdit.setText(cmtf_data.get("enablePlugin"))
            self.m_ui.includePackageLineEdit.setText(cmtf_data.get("includePackage"))
            self.m_ui.includeDataDirLineEdit.setText(cmtf_data.get("includeDataDir"))
            self.m_ui.beforeScriptLineEdit.setText(cmtf_data.get("beforeScript"))
            self.m_ui.afterScriptLineEdit.setText(cmtf_data.get("afterScript"))
            self.m_ui.outputPathLineEdit.setText(cmtf_data.get("outputPath"))
            self.m_ui.removeOutputCheckBox.setChecked(cmtf_data.get("removeOutput"))

    def run_command(self, command, compile_path):
        self.show_log_message(command)

        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=compile_path,
            universal_newlines=True,
        )

        for line in process.stdout:
            self.show_log_message(line)
        process.wait()

    def show_log_message(self, log_text):
        self.m_ui.logPlainTextEdit.insertPlainText(f"{log_text}\n")
        scrollbar = self.m_ui.logPlainTextEdit.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        self.m_ui.statusbar.showMessage(log_text)
        QApplication.processEvents()
