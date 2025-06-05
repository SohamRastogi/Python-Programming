s = {1 , 2 , 5 , 64 , 32 , 6 , "soham"}
s.add(100) # random show, no as such order => Show MUTABLE

print(s)

print(len(s))

s.remove(100)
print(s , len(s))

s.pop() # removes a random element from the set
print(len(s))

# s.clear()  # full set empty 
# print(len(s)) # output would be 0