#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from forms import MainForm
import plugin_manager

def main():
    app, mainForm, window = MainForm.init()
    block_dict = plugin_manager.load()
    mainForm.set_blocks(block_dict)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
