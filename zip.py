s1={1,2,3,4}
s2={'a','b','c','d'}
s3=(list(zip(s1,s2)))
print("zipped list from 2 sets:")
print(s3)
print()

list1=[10, 20, 30 ,40]
list2=[100,300,400,200]

print("Zipping elements with second list reversed:")
for x,y in zip(list1, list2[::-1]):
    print(x,y)
    print()

stocks=['Apple', 'google','Tesla']
prices=[150, 2800, 700]

new_dict={stock:price for stock,price in zip(stocks,prices)}
print('\n{}'.format(new_dict))