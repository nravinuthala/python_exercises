# def sqr(num):
#     return num ** 2

list1 = [1,2,3,4,5]

# list_sqr = list(map(sqr, list1))
sqr = lambda x: x ** 2
list_sqr = list(map(sqr, list1))

print(list_sqr)
# for i in map(sqr, list1):
#     print(i)

