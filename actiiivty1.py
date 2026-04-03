tuplex=("Hello",True, 3.14,10)
print("Tuple with different data types:",tuplex)

tuplex=(1,2,3,4,5)
print("Tuple with integers:",tuplex)

tuplexn=tuplex + (9,)
print("Tuple after concatenation:",tuplexn)

tuplex1=(10,20,30,40,50,50,50,60)
count=tuplex1.count(50)
print("Count of 50 in the tuple:",count)    

tuplex=(0,1,2,3,4,5,6,7,8,9)
slice=tuplex[3:5]
print("Sliced tuple:",slice)

