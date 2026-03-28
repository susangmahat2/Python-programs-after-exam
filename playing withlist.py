L=[2,8,5,9,1,4]
print("The orignal list is:",L)

count=0

for i in L:
    count+=i
    avg=count/len(L)

print("Sum =", count)
print("Average=",avg)

L.sort()

print("Smallest element is:",L[0])
print("Largest element is:",L[-1])
