print("enter marks obtained in five subjects:")

maths= int(input("maths:"))
english= int(input("english:"))
science= int(input("science:"))
hindi= int(input("hindi:"))

sum= maths+english+science+hindi
print("sum of all five subjects is", sum)

perc= (sum/400)*100

print(end="percentage mark=")
print(perc)