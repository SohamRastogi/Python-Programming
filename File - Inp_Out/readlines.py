f = open("file3.txt")
data = f.readlines()
print(data)
f.close()

print(type(data))