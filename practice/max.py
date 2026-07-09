

def my_max( lst):
    maximum = lst[0]

    for i in lst :
        if i >= maximum:
            maximum = i

    return maximum

def my_sum( lst):
    total = 0

    for i in lst :
        total += i

    return total


my_list = [1,3,4,5,6]

print(my_max(my_list))

print(my_sum(my_list))

