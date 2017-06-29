## CODE TO GET/UPDATE THE LATEST TT_SELL RATES OF SBI ##


import tabula
import csv
import numpy as np
import datetime as dt
import os.path;os.remove
import sys


class Data_Work :

	TT_SELL = 0
	Todays_Date = dt.datetime.today().strftime("%d/%m/%Y")
	fieldnames = ['DATE','TT_SELL','TT_BUY']
	final_file = 'sbi_sellrates.csv'


	#df = tabula.read_pdf("https://www.sbi.co.in/webfiles/uploads/files/FOREX_CARD_RATES.pdf")
	try :
		tabula.convert_into("https://www.sbi.co.in/webfiles/uploads/files/FOREX_CARD_RATES.pdf", "output.csv", output_format = "csv")
		with open('output.csv', 'rb') as f:
			getval = csv.reader(f)
			#rows = list(getval)
			a = np.array(list(getval))						#There is a way to do splitting in lists only like :: myList = [i.split()[0] for i in myList]
			#print a[1]										# observation
			#print a[3]										# Euro corresponding Row
			a2 = list(map(float,a[3][2].split())) 			# This is because, the tabula is reading all rates as single variable, but we need TT-sell 
			TT_BUY = a2[0]									# TT_BUY rate 
			TT_SELL = a2[1] 								# SBI TT_SELL RATE FOR THE DAY :: The rate at which inr is converted to eur
			os.remove('output.csv')							# DELETE THE CSV FILE, We only want TT_SELL
	except : 
		print "SBI SITE UNDER MAINTENANCE"		

	############# IF THE FILE ALREADY EXISTS, APPEND THE NEW VALUE THERE ############

	if (os.path.exists("sbi_sellrates.csv") == True) : 
		with open (final_file,'r') as test :
			temp = test.read()						# I AM SO GENIUS !
			if Todays_Date in temp:
				found = True
				print "VALUE ALREADY RECORDED"		# NOTIFY IF THE VALUE IS ALREADY RECORDED !

			else:
				with open(final_file, 'a') as p : 
					writer = csv.DictWriter(p, fieldnames=fieldnames)
					writer.writerow({'DATE': dt.datetime.today().strftime("%d/%m/%Y"), 'TT_SELL': TT_SELL, 'TT_BUY': TT_BUY})

	############# 		OTHERWISE CREATE A NEWFILE AND ADD THERE		 ############
	else:
		with open(final_file, 'w') as p : 
			writer = csv.DictWriter(p, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'DATE': dt.datetime.today().strftime("%d/%m/%Y"), 'TT_SELL': TT_SELL, 'TT_BUY': TT_BUY})

	print "SHEET UPDATED"		