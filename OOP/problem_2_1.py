class TwoDVector :
    
    x = 0
    y = 0

    def getinfo(self) :
        print(self.x , self.y)



class ThreeDVector(TwoDVector):  

    z = 0

    def getInfo2(self) :
        print(self.x , self.y , self.z)

alpha = TwoDVector()
alpha.x  = 10
alpha.y = 20

alpha.getinfo()

beta = ThreeDVector()
beta.x = 15
beta.y = 30
beta.z = 45

beta.getInfo2()



   
        
