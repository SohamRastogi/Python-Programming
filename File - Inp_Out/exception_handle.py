import sys

try : 
    f = open("myfile1.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err :
    print("OSError : ",err)
except ValueError :
    print("conversion to int is an issue here")
except Exception as err :
    print("an unwanted exception came in the way : ",err)
finally :
    print("execution complete")

