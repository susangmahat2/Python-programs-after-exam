try:
    num1,num2=eval(input("Enter two numbers separated by a comma:"))
    result=num1/num2
    print("Result is:",result)
except ZeroDivisionError:
    print("Divisor by zero is error.")
except SyntaxError:
  print("Invalid input. Please enter two numbers separated by a comma.")
except:
   print("wrong error")
else:
   print("No exception")
finally:
   print("this will execute no matter what")         
  