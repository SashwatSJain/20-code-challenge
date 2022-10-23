# Given a string consisting of whitespace and groups of matched
# parentheses, write a Python program to split it into groups of 
# perfectly matched parentheses without any whitespace.

a = "(()) (())"

l, r, n, final_list = 0, 0, "", []

for i in a:
    if i == "(":
        l+=1;n+=i

    elif i == ")":
        r+=1;n+=i

    else:
        print("bad string")
        
    if l == r and l != 0:
        final_list.append(n)
        n = ""

print(final_list)