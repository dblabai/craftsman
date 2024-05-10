import os
import platform
import shutil

from PySide6.QtCore import QStandardPaths

from craftsman.core.constants import SystemConstants


app_support_path = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
resources_path = os.path.join(app_support_path, SystemConstants.APP_NAME)


def get_app_support_path():
    return resources_path


def app_compile_path(app_name: str):
    """Application compilation cache path
    If the folder is not empty, empty it.

    Args:
        app_name (str): Application Name

    Returns:
        str: path
    """
    compile_path = os.path.join(resources_path, "compile", app_name)
    os.makedirs(compile_path, exist_ok=True)
    # Clear folder
    if len(os.listdir(compile_path)) > 0:
        for filename in os.listdir(compile_path):
            file_path = os.path.join(compile_path, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    return compile_path


def python_env_path():
    return os.path.join(resources_path, SystemConstants.ENV, get_bin_name(), "python")


def pip_env_path():
    return os.path.join(resources_path, SystemConstants.ENV, get_bin_name(), "pip")


def get_bin_name():
    if platform.system() == "Windows":
        return "Scripts"
    else:
        return "bin"
