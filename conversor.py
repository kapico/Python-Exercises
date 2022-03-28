pesos = input('How much pesos do you have?: ')
pesos = float(pesos)
value_dollar = 3875
dollars = pesos / value_dollar
dollars = round(dollars, 2)
dollars = str(dollars)
print('you have $' + dollars + 'dollars')