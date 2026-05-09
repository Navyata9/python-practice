units = int(input("enter the number of units consumed: "))

if (units<50 ):
    amount = units*2.60
    suncharge = 25

elif (units<= 100):
    amount = 130 + ((units-50)*3.25)
    suncharge = 50

elif (units <= 200):
    amount = 130 + 162.5 + ((units-100)*5.26)
    suncharge = 45

else:
    amount = 130 + 162.5 + 526 + ((units-200)*8.45)
    suncharge = 75

total = amount + suncharge
print(("\n Electricty Bill = %.2f" %total))