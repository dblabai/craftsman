# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 852)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u":/resources/icon/folder_open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionNuitka = QAction(MainWindow)
        self.actionNuitka.setObjectName(u"actionNuitka")
        self.actionPyInstaller = QAction(MainWindow)
        self.actionPyInstaller.setObjectName(u"actionPyInstaller")
        self.actionCompile = QAction(MainWindow)
        self.actionCompile.setObjectName(u"actionCompile")
        icon1 = QIcon()
        icon1.addFile(u":/resources/icon/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCompile.setIcon(icon1)
        self.actionCompile.setMenuRole(QAction.NoRole)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon2 = QIcon()
        icon2.addFile(u":/resources/icon/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon2)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon3 = QIcon()
        icon3.addFile(u":/resources/icon/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setMenuRole(QAction.NoRole)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon4 = QIcon()
        icon4.addFile(u":/resources/icon/document_add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLabel = QLabel(self.layoutWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.nameLineEdit = QLineEdit(self.layoutWidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.versionLabel = QLabel(self.layoutWidget)
        self.versionLabel.setObjectName(u"versionLabel")

        self.gridLayout.addWidget(self.versionLabel, 1, 0, 1, 1)

        self.versionLineEdit = QLineEdit(self.layoutWidget)
        self.versionLineEdit.setObjectName(u"versionLineEdit")

        self.gridLayout.addWidget(self.versionLineEdit, 1, 1, 1, 1)

        self.versionIncreaseCheckBox = QCheckBox(self.layoutWidget)
        self.versionIncreaseCheckBox.setObjectName(u"versionIncreaseCheckBox")

        self.gridLayout.addWidget(self.versionIncreaseCheckBox, 1, 2, 1, 1)

        self.versionTypeLabel = QLabel(self.layoutWidget)
        self.versionTypeLabel.setObjectName(u"versionTypeLabel")

        self.gridLayout.addWidget(self.versionTypeLabel, 2, 0, 1, 1)

        self.versionTypeComboBox = QComboBox(self.layoutWidget)
        self.versionTypeComboBox.setObjectName(u"versionTypeComboBox")

        self.gridLayout.addWidget(self.versionTypeComboBox, 2, 1, 1, 1)

        self.showVersionTypeCheckBox = QCheckBox(self.layoutWidget)
        self.showVersionTypeCheckBox.setObjectName(u"showVersionTypeCheckBox")

        self.gridLayout.addWidget(self.showVersionTypeCheckBox, 2, 2, 1, 1)

        self.systemLabel = QLabel(self.layoutWidget)
        self.systemLabel.setObjectName(u"systemLabel")

        self.gridLayout.addWidget(self.systemLabel, 3, 0, 1, 1)

        self.systemLineEdit = QLineEdit(self.layoutWidget)
        self.systemLineEdit.setObjectName(u"systemLineEdit")
        self.systemLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.systemLineEdit, 3, 1, 1, 1)

        self.compileModeLabel = QLabel(self.layoutWidget)
        self.compileModeLabel.setObjectName(u"compileModeLabel")

        self.gridLayout.addWidget(self.compileModeLabel, 4, 0, 1, 1)

        self.compileModeComboBox = QComboBox(self.layoutWidget)
        self.compileModeComboBox.addItem("")
        self.compileModeComboBox.addItem("")
        self.compileModeComboBox.setObjectName(u"compileModeComboBox")

        self.gridLayout.addWidget(self.compileModeComboBox, 4, 1, 1, 1)

        self.consoleLabel = QLabel(self.layoutWidget)
        self.consoleLabel.setObjectName(u"consoleLabel")

        self.gridLayout.addWidget(self.consoleLabel, 5, 0, 1, 1)

        self.consoleComboBox = QComboBox(self.layoutWidget)
        self.consoleComboBox.addItem("")
        self.consoleComboBox.addItem("")
        self.consoleComboBox.setObjectName(u"consoleComboBox")

        self.gridLayout.addWidget(self.consoleComboBox, 5, 1, 1, 1)

        self.sourceFilesLabel = QLabel(self.layoutWidget)
        self.sourceFilesLabel.setObjectName(u"sourceFilesLabel")
        self.sourceFilesLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.sourceFilesLabel, 6, 0, 1, 1)

        self.sourceFilesListWidget = QListWidget(self.layoutWidget)
        self.sourceFilesListWidget.setObjectName(u"sourceFilesListWidget")

        self.gridLayout.addWidget(self.sourceFilesListWidget, 6, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sourceFolderPushButton = QPushButton(self.layoutWidget)
        self.sourceFolderPushButton.setObjectName(u"sourceFolderPushButton")
        self.sourceFolderPushButton.setMaximumSize(QSize(24, 24))
        icon5 = QIcon()
        icon5.addFile(u":/resources/icon/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sourceFolderPushButton.setIcon(icon5)

        self.verticalLayout.addWidget(self.sourceFolderPushButton)

        self.sourceFilePushButton = QPushButton(self.layoutWidget)
        self.sourceFilePushButton.setObjectName(u"sourceFilePushButton")
        self.sourceFilePushButton.setMaximumSize(QSize(24, 24))
        icon6 = QIcon()
        icon6.addFile(u":/resources/icon/document_text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sourceFilePushButton.setIcon(icon6)

        self.verticalLayout.addWidget(self.sourceFilePushButton)

        self.sourceRemovePushButton = QPushButton(self.layoutWidget)
        self.sourceRemovePushButton.setObjectName(u"sourceRemovePushButton")
        self.sourceRemovePushButton.setMaximumSize(QSize(24, 24))
        icon7 = QIcon()
        icon7.addFile(u":/resources/icon/subtract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sourceRemovePushButton.setIcon(icon7)

        self.verticalLayout.addWidget(self.sourceRemovePushButton)

        self.verticalSpacer_2 = QSpacerItem(67, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 6, 2, 1, 1)

        self.mainCodeLabel = QLabel(self.layoutWidget)
        self.mainCodeLabel.setObjectName(u"mainCodeLabel")

        self.gridLayout.addWidget(self.mainCodeLabel, 7, 0, 1, 1)

        self.mainCodeLineEdit = QLineEdit(self.layoutWidget)
        self.mainCodeLineEdit.setObjectName(u"mainCodeLineEdit")

        self.gridLayout.addWidget(self.mainCodeLineEdit, 7, 1, 1, 1)

        self.mainCodePushButton = QPushButton(self.layoutWidget)
        self.mainCodePushButton.setObjectName(u"mainCodePushButton")
        self.mainCodePushButton.setMaximumSize(QSize(24, 24))
        self.mainCodePushButton.setIcon(icon6)

        self.gridLayout.addWidget(self.mainCodePushButton, 7, 2, 1, 1)

        self.requirementsLabel = QLabel(self.layoutWidget)
        self.requirementsLabel.setObjectName(u"requirementsLabel")

        self.gridLayout.addWidget(self.requirementsLabel, 8, 0, 1, 1)

        self.requirementsLineEdit = QLineEdit(self.layoutWidget)
        self.requirementsLineEdit.setObjectName(u"requirementsLineEdit")

        self.gridLayout.addWidget(self.requirementsLineEdit, 8, 1, 1, 1)

        self.requirementsPushButton = QPushButton(self.layoutWidget)
        self.requirementsPushButton.setObjectName(u"requirementsPushButton")
        self.requirementsPushButton.setMaximumSize(QSize(24, 24))
        self.requirementsPushButton.setIcon(icon6)

        self.gridLayout.addWidget(self.requirementsPushButton, 8, 2, 1, 1)

        self.iconLabel = QLabel(self.layoutWidget)
        self.iconLabel.setObjectName(u"iconLabel")

        self.gridLayout.addWidget(self.iconLabel, 9, 0, 1, 1)

        self.iconLineEdit = QLineEdit(self.layoutWidget)
        self.iconLineEdit.setObjectName(u"iconLineEdit")

        self.gridLayout.addWidget(self.iconLineEdit, 9, 1, 1, 1)

        self.iconPushButton = QPushButton(self.layoutWidget)
        self.iconPushButton.setObjectName(u"iconPushButton")
        self.iconPushButton.setMaximumSize(QSize(24, 24))
        icon8 = QIcon()
        icon8.addFile(u":/resources/icon/more_horizontal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconPushButton.setIcon(icon8)

        self.gridLayout.addWidget(self.iconPushButton, 9, 2, 1, 1)

        self.enablePluginLabel = QLabel(self.layoutWidget)
        self.enablePluginLabel.setObjectName(u"enablePluginLabel")

        self.gridLayout.addWidget(self.enablePluginLabel, 10, 0, 1, 1)

        self.enablePluginLineEdit = QLineEdit(self.layoutWidget)
        self.enablePluginLineEdit.setObjectName(u"enablePluginLineEdit")

        self.gridLayout.addWidget(self.enablePluginLineEdit, 10, 1, 1, 1)

        self.includePackageLabel = QLabel(self.layoutWidget)
        self.includePackageLabel.setObjectName(u"includePackageLabel")

        self.gridLayout.addWidget(self.includePackageLabel, 11, 0, 1, 1)

        self.includePackageLineEdit = QLineEdit(self.layoutWidget)
        self.includePackageLineEdit.setObjectName(u"includePackageLineEdit")

        self.gridLayout.addWidget(self.includePackageLineEdit, 11, 1, 1, 1)

        self.includeDataDirLabel = QLabel(self.layoutWidget)
        self.includeDataDirLabel.setObjectName(u"includeDataDirLabel")

        self.gridLayout.addWidget(self.includeDataDirLabel, 12, 0, 1, 1)

        self.includeDataDirLineEdit = QLineEdit(self.layoutWidget)
        self.includeDataDirLineEdit.setObjectName(u"includeDataDirLineEdit")

        self.gridLayout.addWidget(self.includeDataDirLineEdit, 12, 1, 1, 1)

        self.beforeScriptLabel = QLabel(self.layoutWidget)
        self.beforeScriptLabel.setObjectName(u"beforeScriptLabel")

        self.gridLayout.addWidget(self.beforeScriptLabel, 13, 0, 1, 1)

        self.beforeScriptLineEdit = QLineEdit(self.layoutWidget)
        self.beforeScriptLineEdit.setObjectName(u"beforeScriptLineEdit")

        self.gridLayout.addWidget(self.beforeScriptLineEdit, 13, 1, 1, 1)

        self.beforeScriptPushButton = QPushButton(self.layoutWidget)
        self.beforeScriptPushButton.setObjectName(u"beforeScriptPushButton")
        self.beforeScriptPushButton.setMaximumSize(QSize(24, 24))
        self.beforeScriptPushButton.setIcon(icon8)

        self.gridLayout.addWidget(self.beforeScriptPushButton, 13, 2, 1, 1)

        self.afterScriptLabel = QLabel(self.layoutWidget)
        self.afterScriptLabel.setObjectName(u"afterScriptLabel")

        self.gridLayout.addWidget(self.afterScriptLabel, 14, 0, 1, 1)

        self.afterScriptLineEdit = QLineEdit(self.layoutWidget)
        self.afterScriptLineEdit.setObjectName(u"afterScriptLineEdit")

        self.gridLayout.addWidget(self.afterScriptLineEdit, 14, 1, 1, 1)

        self.afterScriptPushButton = QPushButton(self.layoutWidget)
        self.afterScriptPushButton.setObjectName(u"afterScriptPushButton")
        self.afterScriptPushButton.setMaximumSize(QSize(24, 24))
        self.afterScriptPushButton.setIcon(icon8)

        self.gridLayout.addWidget(self.afterScriptPushButton, 14, 2, 1, 1)

        self.outputPathLabel = QLabel(self.layoutWidget)
        self.outputPathLabel.setObjectName(u"outputPathLabel")

        self.gridLayout.addWidget(self.outputPathLabel, 15, 0, 1, 1)

        self.outputPathLineEdit = QLineEdit(self.layoutWidget)
        self.outputPathLineEdit.setObjectName(u"outputPathLineEdit")

        self.gridLayout.addWidget(self.outputPathLineEdit, 15, 1, 1, 1)

        self.outputPathPushButton = QPushButton(self.layoutWidget)
        self.outputPathPushButton.setObjectName(u"outputPathPushButton")
        self.outputPathPushButton.setMaximumSize(QSize(24, 24))
        self.outputPathPushButton.setIcon(icon5)

        self.gridLayout.addWidget(self.outputPathPushButton, 15, 2, 1, 1)

        self.removeOutputLabel = QLabel(self.layoutWidget)
        self.removeOutputLabel.setObjectName(u"removeOutputLabel")

        self.gridLayout.addWidget(self.removeOutputLabel, 16, 0, 1, 1)

        self.removeOutputCheckBox = QCheckBox(self.layoutWidget)
        self.removeOutputCheckBox.setObjectName(u"removeOutputCheckBox")

        self.gridLayout.addWidget(self.removeOutputCheckBox, 16, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.layoutWidget1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.logLabel = QLabel(self.layoutWidget1)
        self.logLabel.setObjectName(u"logLabel")

        self.verticalLayout_3.addWidget(self.logLabel)

        self.logPlainTextEdit = QPlainTextEdit(self.layoutWidget1)
        self.logPlainTextEdit.setObjectName(u"logPlainTextEdit")
        self.logPlainTextEdit.setMinimumSize(QSize(0, 180))

        self.verticalLayout_3.addWidget(self.logPlainTextEdit)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuHelp.addAction(self.actionHelp)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionCompile)
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionNuitka.setText(QCoreApplication.translate("MainWindow", u"Nuitka", None))
        self.actionPyInstaller.setText(QCoreApplication.translate("MainWindow", u"PyInstaller", None))
        self.actionCompile.setText(QCoreApplication.translate("MainWindow", u"Compile", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.versionIncreaseCheckBox.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.versionTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Version Type", None))
        self.showVersionTypeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.systemLabel.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.compileModeLabel.setText(QCoreApplication.translate("MainWindow", u"Compile Mode", None))
        self.compileModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"onefile", None))
        self.compileModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"standalone", None))

        self.consoleLabel.setText(QCoreApplication.translate("MainWindow", u"Console Window", None))
        self.consoleComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Enable", None))
        self.consoleComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Disable", None))

        self.sourceFilesLabel.setText(QCoreApplication.translate("MainWindow", u"Source Files", None))
        self.sourceFolderPushButton.setText("")
        self.sourceFilePushButton.setText("")
        self.sourceRemovePushButton.setText("")
        self.mainCodeLabel.setText(QCoreApplication.translate("MainWindow", u"Main Code", None))
        self.mainCodePushButton.setText("")
        self.requirementsLabel.setText(QCoreApplication.translate("MainWindow", u"Requirements", None))
        self.requirementsPushButton.setText("")
        self.iconLabel.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.iconPushButton.setText("")
        self.enablePluginLabel.setText(QCoreApplication.translate("MainWindow", u"Enable Plugin", None))
        self.includePackageLabel.setText(QCoreApplication.translate("MainWindow", u"Include Package", None))
        self.includeDataDirLabel.setText(QCoreApplication.translate("MainWindow", u"Include Data Dir", None))
        self.beforeScriptLabel.setText(QCoreApplication.translate("MainWindow", u"Before Script", None))
        self.beforeScriptPushButton.setText("")
        self.afterScriptLabel.setText(QCoreApplication.translate("MainWindow", u"After Script", None))
        self.afterScriptPushButton.setText("")
        self.outputPathLabel.setText(QCoreApplication.translate("MainWindow", u"Output Path", None))
        self.outputPathPushButton.setText("")
        self.removeOutputLabel.setText(QCoreApplication.translate("MainWindow", u"Remove Output", None))
        self.removeOutputCheckBox.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.logLabel.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

