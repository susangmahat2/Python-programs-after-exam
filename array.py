import array as arr

array=arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array:", str(array))

count_3=array.count(3)
print("Count of 3 in the array:", count_3)
reverse_array=array.reverse()
print("Reversed array:", str(array))
