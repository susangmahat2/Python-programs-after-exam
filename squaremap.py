num1=[1,2,3]
num2=[4,5,6]

result=map(lambda x,y: x+y, num1,num2)
print("Addition of two lists")
print(list(result))

num=[2,3,4,5]

def sq(n):
    return n*n

square=list(map(sq,num))
print("Square of the list")
print(square)
