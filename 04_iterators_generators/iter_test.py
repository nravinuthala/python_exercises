mylist = [100, 200, 300, 400, 500]

print(dir(list))

my_iter = iter(mylist)
# my_iter = mylist.__iter__()
# print(dir(my_iter))
# print(my_iter.__next__())
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))
