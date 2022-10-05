# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QDialog

from .Ui_dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_OK_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass
    
    @pyqtSlot()
    def on_pushButton_Exit_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
