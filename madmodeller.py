#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from forms import MainForm
import plugin_manager as pl

def main():
    app, mainForm, window = MainForm.init()
    block_dict = pl.load()
    mainForm.set_blocks(block_dict)
    mainForm.add_block(block_dict['Gain'])
#    mainForm.add_block(block_dict['Splitter'])
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
