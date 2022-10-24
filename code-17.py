# An irregular/uneven matrix, or ragged matrix,
# is a matrix that has a different number of elements in 
# each row. Ragged matrices are not used in linear algebra,
# since standard matrix transformations cannot be
# performed on them, but they are useful as arrays in computing.
# Write a Python program to find the indices of 
# all occurrences of target in the uneven matrix.

a = [(1,2,3,4,5), (2,3,4,5,6), (3,4,5,6,7), (4,5,6,7,8), (5,6,7,8,9)]
b = []
n = int(input("Enter a number: "))
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == n:
            b.append((i,j))

print(b)