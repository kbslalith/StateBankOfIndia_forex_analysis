from data import Data_Work
import matplotlib.pyplot as plt
import numpy as np
import csv

Data_Work() # FIRST UPDATE THE LATEST VALUE OF TT_SELL IN THE CSV FILE


with open ('sbi_sellrates.csv', 'r') as f:
 	spamreader = csv.reader(f, delimiter=' ', quotechar='|')
 	for row in spamreader:
 		print row 