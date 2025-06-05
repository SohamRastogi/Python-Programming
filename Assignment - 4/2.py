class MyException(Exception):
    def __init__(self, message="General MyException occurred"):
        super().__init__(message)

class FileException(MyException):
    def __init__(self, message="FileException: Error related to file operations"):
        super().__init__(message)


class FileNotFoundException(FileException):
    def __init__(self, message="FileNotFoundException: The specified file was not found"):
        super().__init__(message)


try:
    raise FileNotFoundException() 
except MyException as e:
    print("Caught error : " , e)
