#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Configuration data editor.
"""

# Add module directories to search path
import sys, os.path
thisDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(thisDir, "zgcp"))
sys.path.append(os.path.join(thisDir, "zgcommon"))
sys.path.append(os.path.join(thisDir, "gui"))
#sys.path.append(os.path.join(thisDir, "zgsync"))

from guiConfigEd import GuiConfigEd

import gettext
gettext.install('zeugs', 'i18n', unicode=1)

import framework


def start():
    # Initialize graphical interface
    gui = GuiConfigEd("cfged")

    # enter event loop
    gui.run()

if __name__ == "__main__":
    start()
