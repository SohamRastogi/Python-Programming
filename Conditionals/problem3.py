s = input("enter your comment : ")

# if (s=="Make a lot of money" or s=="buy now" or s=="subscribe this" or s=="click this") :
#     print("the entered message is a spam message")
# else :
#     print("the entered message is not a spam message")

p1 = "Make a mot of money"
p2 = "nuy now"
p3 = "subscribe this"
p4 = "click this"

if((p1 in s) or (p2 in s) or (p3 in s) or (p4 in s)) :
    print("the comment entered is a spam message")
else :
    print("the comment entered is not a spam comment")