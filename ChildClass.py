from Inheritence import CheckData
class ChildClass(CheckData):
    def __init__(self,age,salary):
        super().__init__(age,salary)
        
    
    def showData(self):
        # print("name is",self.name)
        # print("age is",self.age)
        # print("Salary is",self.salary)
        print("Full informations are")
        self.getfullInformation()
        
    
    
obj=ChildClass(40,80000)

obj.showData()
    