from functools import reduce

sum_up = lambda x, y: x + y

list1 = [1,2,3,4,5]

print(reduce(sum_up, list1))