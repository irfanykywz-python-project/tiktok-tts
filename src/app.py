from resources.icons import *
from root_app.globals.const import APPEXE, APPVERSION, ICON
from root_app.globals.style import STYLESHEET
from root_app.controllers.base import Base

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

import os, sys

def main():

    # prepare paramter
    rootDirectory = os.path.dirname(__file__)

    # prepare logging
    """
    add from pyside6-component
    """

    # prepare app
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLESHEET)
    # set icon app
    icon = QIcon(os.path.join(rootDirectory, ICON))
    app.setWindowIcon(icon)

    # prepare window
    window = Base(parentApp=app, rootDirectory=rootDirectory)
    window.show()

    # loop app
    sys.exit(app.exec())

if __name__ == '__main__':
    main()