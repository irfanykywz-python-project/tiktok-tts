import time

from root_app.models.hello.thread import HelloThread
from root_app.views.hello.ui import Hello_UI

from PySide6.QtCore import QTimer, QSettings
from PySide6.QtWidgets import QMessageBox, QFileDialog

import os

class Hello(Hello_UI):

    def __init__(self, parentMain):
        super().__init__()
        self.parentMain = parentMain

    def initUI(self):
        ui = self.setupUI()
        # signal
        self.submitButton.clicked.connect(self.start)

        # statusbar
        self.statusBar.showMessage('tiktok tts by irfanykywz', 5000)
        QTimer.singleShot(2000, lambda: self.statusBar.showMessage('ready'))

        return ui

    def start(self):

        def started():
            self.ttsEditor.setDisabled(True)
            self.voiceSelect.setDisabled(True)
            self.submitButton.setText('Loading...')
            self.submitButton.setDisabled(True)
        def finished():
            self.ttsEditor.setDisabled(False)
            self.voiceSelect.setDisabled(False)
            self.submitButton.setDisabled(False)
            self.submitButton.setText('Buat')
            QTimer.singleShot(2000, lambda: self.statusBar.showMessage('ready'))

        def process(val):
            self.statusBar.showMessage(val)
        def error(val):
            QMessageBox.warning(self, 'Oops!', val)

        # get form data
        text = self.ttsEditor.toPlainText()
        voice = self.voiceSelect.currentText()

        # validation
        if len(text) < 1:
            QMessageBox.warning(self, 'Oops!', 'text masih kosong')
            return None

        # save location
        # https://stackoverflow.com/questions/25490660/remember-path-over-session-in-qfiledialog
        self.settings = QSettings("Company name", "Application name")
        last_path = self.settings.value("LAST_PATH", ".")
        random_file_name = os.path.join(last_path, time.strftime("%H-%M", time.localtime()) + "_" + str(time.time()) + ".mp3")
        path, _ = QFileDialog.getSaveFileName(self, 'pilih lokasi penyimpanan',random_file_name, "Audio Files (*.mp3)")
        self.settings.setValue("LAST_PATH", os.path.dirname(path))

        if path:
            thread = HelloThread(self, {
                'text': text,
                'voice': voice,
                'path': path
            })
            thread.started.connect(started)
            thread.process.connect(process)
            thread.error.connect(error)
            thread.finished.connect(finished)
            thread.start()