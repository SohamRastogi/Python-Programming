class Read_Only_List :
    def __init__(self, num1 ,num2) :
        self.append(num1)
        self.append(num2)
    def append (self , nums) :
        print("appending to the list is not possible.")
   
l1 = Read_Only_List(1,2)




