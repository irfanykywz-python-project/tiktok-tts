from root_app.globals.const import APPNAME, SIZE_X, SIZE_Y

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QMainWindow,
    QFrame,
)
class Base_UI(QMainWindow):

    def __init__(self):
        super().__init__()

        # setup Window
        self.setWindowTitle(APPNAME)
        self.resize(SIZE_X, SIZE_Y)
        # bring window to front
        self.activateWindow()
        self.setWindowState(Qt.WindowState.WindowActive)

    def setupUI(self):

        self.header_layout = QVBoxLayout()
        """
        add your widget for header
        """

        self.body_stacked = QStackedWidget()
        self.body_layout = QVBoxLayout()
        """
        add your widget for body
        """
        self.body_layout.addWidget(self.body_stacked)


        self.footer_layout = QHBoxLayout()
        """
        add your widget for footer
        """

        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(self.header_layout)
        main_layout.addLayout(self.body_layout)
        main_layout.addLayout(self.footer_layout)

        centralWidget = QFrame()
        centralWidget.setLayout(main_layout)
        self.setCentralWidget(centralWidget)