class Marks :
    def __init__ (self , marks) :
        self.marks = marks

    def update_marks_by (self , addition_of_marks , obj) :
        self.marks = self.marks + addition_of_marks
        print("change of marks has been done successfully : ")
        print(f"updated marks of {obj} are ", self.marks)

m1 = Marks(10)
m2 = Marks(12)

print("original marks of the student m1 are : ", m1.marks)
print("original marks of the student m2 are : ", m2.marks)

m1.update_marks_by(2 , "m1")
m2.update_marks_by(4 , "m2")




