import sys

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import PySide6.QtAsyncio as QtAsyncio

from craftsman.core.constants import SystemConstants
from craftsman.home_module.home import MainWindow

import craftsman.resources.resources_rc

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_UseSoftwareOpenGL)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/resources/icon/craftsman.png"))
    window = MainWindow()
    window.setWindowTitle(SystemConstants.APP_NAME)
    window.resize(800, 600)
    window.show()
    
    QtAsyncio.run()
