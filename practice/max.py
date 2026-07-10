

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

def rev_arr(lst):
    temp_arr = []

    for i in range(len(lst) -1 , -1 , -1):
        temp_arr.append(lst[i])

    return temp_arr

def remove_duplicates(lst):
    temp = list(set(lst))

    return temp

def count_char(text):

    count = 0
    for i in text:
        count += 1
    return count

def is_anagram(str1, str2):

    return sorted(str1) == sorted(str2)

my_list = [1,3,4,5,6,6]

print(my_max(my_list))

print(my_sum(my_list))

print(rev_arr(my_list))

print(remove_duplicates(my_list))

print(count_char("college"))

print(is_anagram("uma", "amu"))