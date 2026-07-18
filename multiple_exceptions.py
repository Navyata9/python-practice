try:
    num_1, num_2= eval(input("Enter two numbers seperated by a comma:"))
    result= num_1/num_2
    print("result is:", result)

except ZeroDivisionError:
    print("Division by zero is not allowed!")

except SyntaxError:
    print("Comma is missing. Enter two number seperated by a comma like this 1,2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what.")