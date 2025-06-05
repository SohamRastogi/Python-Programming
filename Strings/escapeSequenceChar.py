# about \n character => new line lagata hai
s = """soham is a good boy 
but not a bad boy"""

print(s)

# OR

s = "soham is a good boy \nbut not a bad boy"
print(s)

#about \t character => tab jitni space give

str = "soham is a good boy\tbut not a bad boy"
print(str)

# want to use double quotes in the string , here's the way
string = "soham is a good \"boy\" but not a bad \"boy\""
print(string)

# want to use single quotes in the string, here's the way
strings = "soham is a good 'boy' but not a bad 'boy'"
print(strings)

# error =>
# s = 'soham is a good boy but not a bad 'boy''

#want to use single quotes in a string made with single quotes, here's the way out
s = 'soham is a good boy but not a bad \'boy\''
print(s)

# want to use backslash in a string -> always use by \\ instead of \ for avoiding errors in all the cases.
s = "hello \\world"
print(s)