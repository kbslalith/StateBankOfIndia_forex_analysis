

import datetime as dt
Todays_Date = dt.datetime.today().strftime("%d/%m/%Y")

#print Todays_Date
with open ('sbi_sellrates.csv','r') as test :
	s = test.read()
	if Todays_Date in s:
		found = True
		print "YEAAA BIAATCH"

	else:
		print "Kuch tho gudbad hei"