# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QDialog

from .Ui_dialog import Ui_Dialog

import asyncio
from websocket import client

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
        client_recv = asyncio.run(client.light(set_status = "on"))
        self.label_Log.setText(f"从服务端获取的信息：{client_recv}")
        pass
    
    @pyqtSlot()
    def on_pushButton_Exit_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        client_recv = asyncio.run(client.light(set_status = "quit"))
        self.label_Log.setText(f"从服务端获取的信息：{client_recv}")
        self.close()
