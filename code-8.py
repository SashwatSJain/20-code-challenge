# Write a Python program to find list integers containing
# exactly four distinct values, such that no integer 
# repeats twice consecutively among the first twenty entries


dval = []
lst = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
for i in range(1,21):
    if lst[i-1] not in dval:
        dval.append(lst[i-1])

if len(dval) == 4:
    for j in range(1,19):
        if lst[j] == lst[j-1]:
            print("pass")

else:
    print("fail")
