print("Enter an number(numerator):")
numn= int(input())

print("Enter an number(denominator):")
numd= int(input())

if numn%numd==0:
    print("\n" +str(numn)+" is divisible by " +str(numd))
else:
    print("\n" +str(numn)+" is not divisible by " +str(numd))