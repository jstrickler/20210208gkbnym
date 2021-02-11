#!/usr/bin/env python
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_bnymdemo import Ui_BYNMdemo

class AppNameMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_BYNMdemo()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

    # Connect up buttons.
        self.ui.bt_go.clicked.connect(self._handle_go)
        self.ui.bt_stop.clicked.connect(self._handle_stop)

    def _handle_go(self):
        self.ui.le_something.setText("GO GO GO")

    def _handle_stop(self):
        self.ui.le_something.setText("Oh, STAHP")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AppNameMain()
    main.show()
    app.exec()


