actual_amount= float(input("Please enter the actual sale price:"))
sale_amount= float(input("Please enter the sales amount:"))

if (sale_amount> actual_amount):
    amount= sale_amount- actual_amount
    print("The total prifit is", amount)

else:
    print("No Profit!")