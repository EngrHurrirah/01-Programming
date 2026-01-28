weight = input ('What is your weight ?: ')
unit = input ('Is this in (K)g or (L)bs ?: ')
if unit.upper() == 'K' or 'KG':
    converted = float(weight) / 0.45
    print (f'You are {converted} Lbs')
elif unit.upper() == 'L' or 'LBS':
    converted = float(weight) * 0.45
    print (f'You are {converted} Kgs')
else:
    print ('Please enter a valid unit (K)g or (L)bs')