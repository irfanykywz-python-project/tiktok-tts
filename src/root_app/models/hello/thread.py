from root_app.utils.tts_tiktok import tts_tiktok

from PySide6.QtCore import QThread, Signal

import time

class HelloThread(QThread):

    process = Signal(tuple)
    error = Signal(tuple)

    def __init__(self, parent, payload):
        super().__init__(parent)
        self.parent = parent
        self.payload = payload

    def run(self):
        print(self.payload['text'])
        print(self.payload['voice'])
        print(self.payload['path'])

        self.process.emit(str('sedang membuat audio...'))
        time.sleep(0.025)

        try:
            tts_tiktok(self.payload['text'], self.payload['voice'], self.payload['path'])
            self.process.emit(str('berhasil membuat audio'))
            time.sleep(0.025)
        except Exception as e:
            self.process.emit(str('gagal membuat audio, ulangi'))
            self.error.emit(str(e))