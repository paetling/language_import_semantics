import sys

print sys.path

from subpackage.hello import cat
from subpackage.goodbye import dog

animal = 1

print('animal', animal)
