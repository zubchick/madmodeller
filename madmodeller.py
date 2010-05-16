#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from forms import MainForm
import plugin_manager as pl

def main():
    app, mainForm, window = MainForm.init()
    mainForm.set_blocks(pl.load())
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
