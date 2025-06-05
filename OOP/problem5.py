class Train_ticket :
    book = ""
    status = ""
    price = 0

    def __init__(self , book , status , price) :
        self.book = book
        self.status = status
        self.price = price

    def getinfo(self) :
        print(f"the user request is {self.book}, the status of the seat is {self.status} and the price of the seat is {self.price}")



t = Train_ticket("book my ticket" , "booked" , 2500) 

t.getinfo()
