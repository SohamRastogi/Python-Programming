username = "chaiaurcode"

def func() :
    username = "chai"  # local variable, outside username is still "chaiaurcode".
    print(username)

print(username)
func()
print(username)