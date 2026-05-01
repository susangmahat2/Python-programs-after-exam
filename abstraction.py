from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("Value passed:", x)
    @abstractmethod
    def task(self):
        print("This is an abstract method")
class test_class(Absclass):
    def task (self):
        print("we are in the  test_class")        

test_obj = test_class()
test_obj.task()
test_obj.print(1000)        
