from data import Data_Work
import matplotlib.pyplot as plt
import numpy as np
import csv
from forex_python.converter import CurrencyRates
import datetime as dt
import time

fieldnames = ['DATE_TIME','TT_SELL']


def mainsheet():
	try :
		Data_Work() # FIRST UPDATE THE LATEST VALUE OF TT_SELL IN THE CSV FILE
	except:
		pass

hours = 0
days = hours/24

c = CurrencyRates()
rate = c.get_rate('EUR', 'INR')
x = 1
with open('hourlyrates.csv','a') as x:
	writer = csv.DictWriter(x, fieldnames=fieldnames)
	writer.writeheader()

def liverates():
	c = CurrencyRates()
	rate = c.get_rate('EUR', 'INR')
	with open('hourlyrates.csv','a') as x:
		writer = csv.DictWriter(x, fieldnames=fieldnames)
		writer.writerow({'DATE_TIME': dt.datetime.today().strftime("%d/%m/%Y %H"+"hrs"), 'TT_SELL': rate })


while True:
	liverates()
	time.sleep(3) #SHOULD BE 3600 FOR ONE HOUR
	hours += 1
	# if (hours == 3): #SHOULD BE 24 FOR ONE DAY
	# 	mainsheet()
	# 	print "I AM HERE NOW"
	# 	hours = 0
	 






