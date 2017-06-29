
# Implementing exception handling

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
