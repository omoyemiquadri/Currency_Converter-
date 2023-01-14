from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount you want to convert: "))
from_curency = input("From Currency: ").upper()
to_currency = input("To Currrency: ").upper()
print(amount, from_curency, "to", to_currency)
result = c.convert(from_curency, to_currency, amount)
print(result)