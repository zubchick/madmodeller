#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from forms import MainForm

def main():
    app, mainForm, window = MainForm.init()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
