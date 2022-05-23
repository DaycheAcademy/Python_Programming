# Refere to :
# https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355
# https://careerkarma.com/blog/what-is-init-py/

# import myPackage
from myPackage import m1
from myPackage.m2 import func2

import myPackage

print(myPackage)

import sys
sys.path.insert(0, '.\\testDirectory')
import random
import mod
# from mod import myList as ml
from mod import *

# --------------
# Alias OR Alternate
# import pandas as pd
# import numpy as np
# import tensorflow as tf
# --------------

# Python Search Path:
# 1 - Current Directory
# 2 - PYTHONPATH: --> OS dependent => Environment Variables
# 3 - Installation Dependent Path

print(sys.path)
# print(random.randint(1, 10))

print(random.a)
print(sys.path)

# ===========================
print('=' * 40)
print(mod.myString)
# print(ml)

# namespace
temVar = 1, 2, 3
print(dir())

# ===========================
print('=' * 40)

m1.func1('foo')
func2('foo')








