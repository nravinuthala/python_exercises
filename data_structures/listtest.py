list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list1 = [x if x % 2 == 0 else x + 1 for x in list1]
print(list1)

list1 = [x for x in list1 if x % 2 == 0]
print(list1)

sqrs = [x ** 2 for x in list1]
print(sqrs)

doubles = [x * 2 for x in list1] 
print(doubles)

cubes = [x ** 3 for x in list1]
print(cubes)

cubes = [x ** 3 for x in range(1, 10)]
print(cubes)


# tpl1 = (1,2,3)
# sqrst = tuple((x ** 2 for x in tpl1))
# print(sqrst)
# print(type(sqrst))
# for i in sqrst:
#     print(i)


