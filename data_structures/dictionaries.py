# emp1 = {
#     "name": "John", 
#     "age":25, 
#     "salary": 40000
# }

# emp2 = dict()

# emp2["name"] = "Jane"
# emp2["age"] = 30
# emp2["salary"] = 60000

# print(emp1)
# print(emp2)

# print(emp1["name"])

# emp1["salary"] = 50000

# print(emp1)
# key1 = "name"
# key2 = "city"
# print(key1 in emp1)
# print(key2 in emp1)

# for key in emp1:
#     # print(key)
#     print(f"{key}: {emp1[key]}")

# print(dir(emp1))

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# emp1.clear()
# print(emp1)

# emp1 = {
#     "name": "John", 
#     "age":25, 
#     "salary": 40000,
#     "certifications": ["AWS", "Azure", "Python"]
# }

# from copy import deepcopy
# emp4 = deepcopy(emp1)

# # emp3 = emp1.copy()
# print("Before updating original")
# print("Original")
# print(emp1)
# print("Deep Copy")
# print(emp4)

# emp1["salary"] = 50000
# emp1["certifications"][-1] = "Java"
# # print("After updating original")
# # print("Original")
# # print(emp1)
# # print("Copy")
# # print(emp3)



# print("After updating original")
# print("Original")
# print(emp1)
# print("Deep Copy")
# print(emp4)


# emp1 = {
#     "name": "John", 
#     "age":25, 
#     "salary": 40000,
#     "certifications": ["AWS", "Azure", "Python"]
# }

# print(emp1["name"])
# print(emp1.get("name"))

# print(emp1.get("name1"))
# print(emp1["name1"])

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# print(emp1.items())

# for i in emp1.items():
#     print(i)

# for k in emp1.keys():
#     print(k)

# for v in emp1.values():
#     print(v)

# name = emp1.pop("name")
# print(name)
# print(emp1)

# last_item = emp1.popitem()
# print(last_item)
# print(emp1)

emp1 = {
    "name": "John", 
    "age":25, 
    "salary": 40000
}
certs = {
    "certifications": ["AWS", "Azure", "Python"]
}
print(emp1)
emp1.update(certs)
print(emp1)