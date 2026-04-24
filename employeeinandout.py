class Employee:
    def __init__(self):
        print("Employee class created")
    def __del__(self):
        print("Destructor called")    
def create_obj():
    print("Making Object..")
    obj=Employee()
    return obj
print("Calling create_obj() function")
obj=create_obj()
print("Program Ended")


