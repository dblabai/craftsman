from PySide6.QtWidgets import QMessageBox


def show_message(message: str):
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Meaages")
    msg_box.setText(message)
    msg_box.exec()
