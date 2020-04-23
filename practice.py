import math
'''milesPerGallon = 20 #float(input()) 
dollarsPerGallon = 3.1599 #float(input())

miles_20 = (20 / milesPerGallon) * dollarsPerGallon
miles_75 = (75 / milesPerGallon) * dollarsPerGallon
miles_500 = (500 / milesPerGallon) * dollarsPerGallon


print(str(miles_20) + " " + str(miles_75) + " " str(miles_500))'''

import math


age = input()
weight = input()
hr = input()
time = input()

womens_cal = ((age * 0.074) - (weight * 0.05741) +
              (hr * 0.4472) - 20.4022) * (time / 4.184)
mens_cal = ((age * 0.2017) + (weight * 0.09036) +
            (hr * 0.6309) - 55.0969) * (time / 4.184)

print(womens_cal)
print(mens_cal)
