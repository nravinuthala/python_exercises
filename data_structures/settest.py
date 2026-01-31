# colors = {"green", "pink", "blue", "green"}
# print(colors)

# for i in colors:
#     print(i)

# print(dir(colors))

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

# colors.add("purple")
# print(colors)

# colors.clear()
# print(colors)

# print(colors[0])

# colors_copy = colors.copy()
# print(colors_copy)

# empty_set = set()
# print(type(empty_set))

# colors_list = list(colors)
# print(colors_list)

# list_with_duplicates = [4,4,4,5,5,5,6,6,6,1,1,1,2,2,2,3,3,3]
# print(list_with_duplicates)
# set1 = set(list_with_duplicates)
# print(set1)

# list_without_duplicates = list(set1)
# print(list_without_duplicates)

set1 = {29,26,53,94,53,63}
set2 = {4,5,6,7,8,9}

print(f"set1 is {set1}")
print(f"set2 is {set2}")
# print(set1.difference(set2))

# set1_2 = set2.difference(set1)
# print(set1_2)

# set1.difference_update(set2)
# print(set1)

# int_set = set1.intersection(set2)
# print(int_set)

# set1.intersection_update(set2)
# print(f"set1 after intersection update {set1}")
# print(set2)

# set2.intersection_update(set1)
# print(f"set2 after intersection update {set2}")
# print(set1)
# set3 = {100,200,300}
# print(set1.isdisjoint(set2))
# print(set1.isdisjoint(set3))

# set4 = {7,8,9}
# print(set1.issubset(set2))
# print(set4.issubset(set2))
# print(set2.issuperset(set4))

# set1.discard(1)
# set1.discard(100)
# print(set1)

# val = set1.pop()
# print(val)

colors = {"blue", "pink", "green"}
print(colors)
# print(colors.pop())
colors.discard("green1")
colors.remove("pink")
print(colors)


