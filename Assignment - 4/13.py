class File_Reader :

    def file_function (self , file_name) :
        try :
            f = open(f"{file_name}" , "r")
            content = f.read()
            print(content)
            f.close()
        except OSError as err :
            print("OsError : ", err)

f1 = File_Reader()

# can give .csv extension files also, if the given file does not exist, OS Error occurs.
f1.file_function ("ans13.txt")


