from data import Data_Work
import matplotlib.pyplot as plt
import numpy as np
import csv
from forex_python.converter import CurrencyRates

Data_Work() # FIRST UPDATE THE LATEST VALUE OF TT_SELL IN THE CSV FILE
c = CurrencyRates()
rate = c.get_rate('EUR', 'INR')

print rate

