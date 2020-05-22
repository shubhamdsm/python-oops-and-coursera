#attributes and methods
# class- class is a blueprint for creating instances
# instance- each employee we create will be the instance of the class.
#__init__ meaning initialize
# self is an instance
# methods we create automatically take instance which is called fork.


class employee:
    def __init__(self,first,last,pay): #self is instance of the class
        self.first=first #instance variable
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1=employee('shubham','yadav',50000) #the emp1 is instance of the class
emp2=employee('dinesh','yadav',60000)  #the emp2 is instance of the class

#print(employee.fullname(emp1))
print(emp1.fullname())



