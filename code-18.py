# Write a Python program to check, for each 
# string in a given list, whether the last 
# character is an isolated letter or not. 
# Return True or False

a = ["the", "list", "of", "string s"]

for i in a:
    if i[-1].isalpha() and i[-2] == " ":
        print("True")
    else:
        print("False")