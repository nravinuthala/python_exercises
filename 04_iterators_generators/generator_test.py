def even_num_generator():
    print("Hello")
    for i in range(5):
        yield i * 2 # the control stays here till next is called again

# for j in even_num_generator():
#     print(j)

my_iter = iter(even_num_generator())

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

