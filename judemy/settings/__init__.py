__author__ = 'k1'

from base import *

try:
    from local import *
    live = False
except:
    live = True

if live:
    from production import *