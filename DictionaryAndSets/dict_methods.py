marks = {
    "Harry" : 100,
    "shubham" : 56,
    "rohan" : 23,
    0 : "Harry"
}

print(marks.items())
print(marks)
print(marks.keys())
print(marks.values())

marks.update({"Harry" : 99})  #  dictionary => mutable
marks.update({"Renuka" : 100})
print(marks)

print(marks.get("Harry"))
print(marks.get("Soham")) # as soham is not present : None is the output for this case

# imp difference
# print(marks.get("soham")) => returns None
# print(marks["soham"]) => returns an error

value = marks.pop("Harry"),
print(value)
print(marks)

print(len(marks))