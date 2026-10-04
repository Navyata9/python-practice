class Employee:

    def __init__(self):
        print("employee created")

    def  __del__(self):
        print("Destructor called")

def Create_obj():
    print("Making object...")
    obj= Employee()
    print("function end")
    return obj

print("Calling Create_obj() function")
obj1= Create_obj()
print("Program End")
