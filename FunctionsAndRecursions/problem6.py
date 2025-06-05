l = ["soham" , "rastogi" , "name" , "shresth" , "shaurya" , "pratinav" , "gupta" , "goel" , "vishwakarma" , "prakhar" , "Bajpayee"]

def remove(string) :
    if(string in l) : 
        l.remove(string)
    
remove("ssoham") 

print(l)