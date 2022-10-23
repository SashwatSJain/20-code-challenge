# We are making n stone piles! The first pile has n stones. 
# If n is even, then all piles have an even number of stones. 
# If n is odd, all piles have an odd number of stones. 
# Each pile must more stones than the previous pile but as few as possible. 
# Write a Python program to find the number of stones in each pile.

n = int(input("n: "))
last_layer = n
layers = []

for i in range(1, n+1):
    
    layers.append(last_layer)
    last_layer+=2
print(layers)