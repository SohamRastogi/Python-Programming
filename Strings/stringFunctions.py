name = "Soham"
print(len(name))

print(name.endswith("am"))
print(name.endswith("an"))

print(name.startswith("So"))
print(name.startswith("soh"))

word = "basic python programming course"  
print(word.capitalize()) # only capitalize the first letter of the line
print(word.title()) # capitalize every first letter of each word

word1 = "soham"
print(word1.upper())

word2 = "HELLO"
print(word2.lower())

s = "hello world"
index = s.find("world")
print(index)
index = s.find("e")
print(index)

replaced_string = s.replace("world" , "python") # replace all occurences of world with python
print(replaced_string)

charstr = "hello world world"
replaced_charstr = charstr.replace("world" , "python")
print(replaced_charstr)
