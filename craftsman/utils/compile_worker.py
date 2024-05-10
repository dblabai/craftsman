import subprocess
import shlex
from PySide6.QtCore import QObject, Slot, Signal


class CompileWorker(QObject):
    finished = Signal()
    stdout = Signal(str)

    async def start(self, command, compile_path):
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=compile_path,
            universal_newlines=True,
        )

        for line in process.stdout:
            self.stdout.emit(line)

        process.wait()
        self.finished.emit()
