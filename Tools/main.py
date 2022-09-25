# -*- coding: utf-8 -*-

"""
main
"""

from PyQt6 import QtWidgets
import sys

from ui.dialog import Dialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())
