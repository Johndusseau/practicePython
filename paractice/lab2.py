import math

age = input()
weight = input()
hr = input()
time = input()

womens_cal = ((age * 0.074) - (weight * 0.05741) +
              (hr * 0.4472) - 20.4022) * (time / 4.184)
mens_cal = ((age * 0.2017) + (weight * 0.09036) +
            (hr * 0.6309) - 55.0969) * (time / 4.184)

print('womens: {:.2f} calories' .format(womens_cal))
print('mens: {:.2f} calories' .format(mens_cal))
