import array as arr

my_arr = arr.array('i' , [1,2,3,4,5])

print("Array Elements : ")
for i in range(len(my_arr)):
    print(my_arr[i])


print(my_arr)
print(my_arr.typecode)

print(my_arr.reverse())

my_arr.insert(3 , 44)
print(my_arr)

my_arr.append(55)
print(my_arr)

my_arr[4] = 1234
print(my_arr)

my_arr.pop(2)
print(my_arr)

my_arr.remove(1)
print(my_arr)



