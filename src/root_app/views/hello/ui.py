
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QStatusBar,
    QPushButton,
    QTextEdit,
    QComboBox,
)

class Hello_UI(QFrame):

    def setupUI(self):

        self.ttsEditor = QTextEdit(self)
        self.ttsEditor.setPlaceholderText('masukan text yang akan dijadikan suara')
        self.voiceSelect = QComboBox(self)
        self.voiceSelect.addItems([
            # "id_001", # this same as female noor
            "id_female_noor",
            "id_male_darma",
            "id_female_icha",
            "id_male_putra",
        ])
        self.submitButton = QPushButton('Buat')
        self.statusBar = QStatusBar(self)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.ttsEditor)
        layout.addWidget(self.voiceSelect)
        layout.addWidget(self.submitButton)
        layout.addWidget(self.statusBar)

        self.setLayout(layout)
        return self