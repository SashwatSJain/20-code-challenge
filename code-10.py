# Write a Python program to find the indexes 
# of numbers of a given list below a given threshold.

a = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
b = []
for i in range(len(a)):
    if a[i] < 50:
        b.append(i)
print(b)