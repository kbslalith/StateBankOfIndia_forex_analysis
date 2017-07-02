from forex_python.converter import CurrencyRates

c = CurrencyRates()
rate = c.get_rate('EUR', 'INR')

print rate
