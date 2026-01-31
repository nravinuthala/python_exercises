n = int(input())
 
last_char = ord('A') + n
 
for i in range(1, n + 1):
    for j in range(i):
        print(chr(last_char - j), end="")
    print()