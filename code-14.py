# Write a Python program find the longest
#  string of a given list of strings.

a = ["this", "is", "a", "list", "of", "strings"]

b = 0
for i in a:
    if len(i) > b:
        b = len(i)
        c = i

print(c)