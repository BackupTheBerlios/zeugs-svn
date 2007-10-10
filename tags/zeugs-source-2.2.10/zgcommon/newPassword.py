#!/usr/bin/env python
# -*- coding: utf-8 -*-

#2007-06-25
# Copyright 2007 Michael Towers

# This file is part of Zeugs.
#
# Zeugs is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Zeugs is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zeugs; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#
"""A simple dialog to fetch a password.
"""
# pyuic4 command:
#      pyuic4 -o ui_dlg_pw.py dlg_pw.ui

# To convert the i18n stuff to gettext form, use gettextify, e.g.
#      gettextify ui_dlg_pw.py

from PyQt4 import QtCore, QtGui

import ui_dlg_pw as ui_dlg

class PWGui(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = ui_dlg.Ui_Dialog()
        self.ui.setupUi(self)
        self.result = None

    @QtCore.pyqtSignature("")
    def on_pushButton_accept_clicked(self):
        p1 = unicode(self.ui.lineEdit_1.text())
        p2 = unicode(self.ui.lineEdit_2.text())
        if (p1 == p2):
            self.result = p1
            self.close()
        else:
            message(_("Passwords don't match, try again"))

    @QtCore.pyqtSignature("")
    def on_pushButton_cancel_clicked(self):
        self.close()


def getPassword():
    Dialog = PWGui()
    Dialog.exec_()
    return Dialog.result




