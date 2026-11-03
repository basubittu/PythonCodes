class Square:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def areaOfSquare(self):
        self.area=(self.length*self.breadth) 
        print("Area of the square is",self.area)    
    
    
class Quoboid(Square):
    def __init__(self,l,b,h):
        self.h=h
        super().__init__(l,b)
    
    def  volume(self):
        self.volume=(self.length*self.breadth*self.h)
        print("Volume is",self.volume)
        
        


r=Quoboid(10,20,30)
r.volume()