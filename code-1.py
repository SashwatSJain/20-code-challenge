# Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
l = []
while True:
    # loop to create list
    a = input("enter number : ")
    if a.isnumeric():
        l.append(int(a))

    else:
        break

print("List: ",l)
if l.count(19) == 2 and l.count(5) >= 3:
    print("True")
else:
    print("False")
