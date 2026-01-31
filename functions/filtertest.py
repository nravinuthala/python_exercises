def even_finder(i):
    return i % 2 == 0

list1 = [1,2,3,4,5,6,7,8]

even_list = list(filter(even_finder, list1))

print(even_list)

even_list2 = list(filter(lambda x: x % 2 == 0, list1))

print(even_list2)