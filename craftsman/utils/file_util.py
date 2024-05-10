import os
from pathlib import Path
import re
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QFileDialog


def open_select_folder(original_folder_path: str = ""):
    if not original_folder_path.strip():
        original_folder_path = str(Path.home() / "Desktop")

    original_folder_path = QFileDialog.getExistingDirectory(
        None,
        QCoreApplication.translate("utils", "Select folder", None),
        original_folder_path,
    )
    return original_folder_path


def open_select_file(file_path: str, file_type: str):
    if not file_path.strip():
        file_path = str(Path.home() / "Desktop")

    file_path, _ = QFileDialog.getOpenFileName(
        None,
        QCoreApplication.translate("utils", "Select File", None),
        file_path,
        file_type,
    )
    return file_path


def match_files_with_extensions(folder_path, extensions):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extensions):
                return os.path.join(root, file)
    return None


def match_file(folder_path, file_name):
    match_file_path = os.path.join(folder_path, file_name)
    if os.path.exists(match_file_path):
        return match_file_path
    return None


def find_first_file_with_pattern(folder_path, pattern):
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            if re.search(pattern, filename, re.IGNORECASE):
                return os.path.join(root, filename)
    return None
