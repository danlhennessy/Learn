# Efficient data type for handling large numbers of basic values (Can only store int, float, str)
from array import array
from random import random

floats = array('d', (random() for i in range(800)))  # 'd' is typdecode to signify double-precision floats
print(floats[3])