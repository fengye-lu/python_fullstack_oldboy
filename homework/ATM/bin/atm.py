# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 13:59
# @Author  : Jackey-lu
# @File    : atm.py

import os, sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from core import main
if __name__ == '__main__':
    main.run()
