# Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.

a = int(input("Enter a number: "))

if a>4**4 and a%34 == 4:
    print("True")
else:
    print("False")
