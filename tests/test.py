from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
import PySide6.QtAsyncio as QtAsyncio
import asyncio
import sys

class TextSetter(QObject):
    # Define a new signal
    text_set_complete = Signal()

    async def set_text(self, label):
        await asyncio.sleep(3)
        label.setText("What do you get if you multiply six by nine?")
        # Emit the signal to indicate text setting is complete
        self.text_set_complete.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        self.text = QLabel("The answer is 42.")
        layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignCenter)

        async_trigger = QPushButton(text="What is the question?")
        async_trigger.clicked.connect(self.set_text_async)
        layout.addWidget(async_trigger, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create an instance of TextSetter
        self.text_setter = TextSetter()
        # Connect the TextSetter's signal to a slot
        self.text_setter.text_set_complete.connect(self.on_text_set_complete)

    def set_text_async(self):
        # Call the set_text method of TextSetter when the button is clicked
        asyncio.ensure_future(self.text_setter.set_text(self.text))

    def on_text_set_complete(self):
        # Code to execute after text is set
        print("Text has been set.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    QtAsyncio.run()
