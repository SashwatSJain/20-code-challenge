# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.

a = str(input("enter string : "))
strng = ""
srng = []
spr = []
for i in a:
    if i.isalpha():
        strng+=i
    
    else:
        srng.append(strng)
        spr.append(i)
        pass
print(srng)
print(spr)