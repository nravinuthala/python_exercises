# lang = "python"
# print(lang)

# print(lang.capitalize())
# print(lang)

# print(dir(str))

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 
# 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
# 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

lang1 = 'PYTHON'
lang2 = 'python'
lang3 = 'Python'
# print(lang1.casefold())
# print(lang2.casefold())
# print(lang3.casefold())

# print(lang1.casefold() == lang2.casefold())

lang11 = lang1.center(50, '*')
# print(len(lang11))
# print(lang1)
# print(lang1.center(50, '*'))

# print(lang11.count('*'))
# print(lang2.count('hon'))

# char = 'a'
# en_char = char.encode('utf-8')
# # print(char.encode('ASCII'))
# print(type(en_char))
# # print(ord(char))
# char1 = en_char.decode()
# print(char1)
# print(type(char1))

mailid = "nravinuthala@gmail.com"
# print(mailid.endswith('com')) # prints True
# print(mailid.endswith('com1')) # prints False

# print(mailid.startswith('nr')) # prints True
# print(mailid.startswith('kr')) # prints False

# print(mailid.find('n')) # prints 0
# print(mailid.find('com')) # prints 19
# print(mailid.find('z')) # prints -1

# print(mailid.index('n')) # prints 0
# print(mailid.index('com')) # prints 19
# print(mailid.index('z')) # gives error

# char1 = 'a'
# char2 = 'A'
# num1 = '0'
# spchar = '#'
# print(char1.isalnum())
# print(char2.isalnum())
# print(num1.isalnum())
# print(spchar.isalnum())

# print(char1.isalpha())
# print(char2.isalpha())
# print(num1.isalpha())
# print(spchar.isalpha())

# print(char1.isdigit())
# print(num1.isdigit())

# words = ["hi", "how", "are", "you?"]

# string = " ".join(words)

# print(string)

# string = "hi*how*are*you?"
# words = string.split("*")
# print(words)

# string = "       python            "
# print(string)
# print(len(string))
# new_string = string.strip()
# print(new_string)
# print(len(new_string))

# string = "python"
# new_string1 = string.ljust(50, "*")
# print(new_string1)

# new_string2 = string.rjust(50, "*")
# print(new_string2)

# new_string2 = string.center(50, "*")
# print(new_string2)

# string = "python"
# new_string = string.replace("hon", "HON")
# print(new_string)

# string = "python iS A bEAUtifUL lANGUAge"
# new_string = string.swapcase() # changes lowercase into uppercase and vice versa
# print(new_string)

string = "python isabeautifullanguage"
# new_string1 = string.capitalize() # makes first letter as uppercase
# new_string2 = string.title() # makes first letter of every word as uppercase

# print(new_string1)
# print(new_string2)

print(min(string))
print(max(string))