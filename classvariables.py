#class variable- class variable are those vairable which are shared among all instances of a class. Class variable are same for each instance
#instance variable - instance variable are unique for each instance of a class
# if we want to access the class variable either we can access it from class or access from the instance of the class (Self)
# instances dont have the class variable so it checks the class which it inherits from .
# if we assign class variable through an instance it only changes that value of that variable


class employee:

    numofemps=0#class variables
    raise_amt=1.04
    def __init__(self,first,last,pay): #self is instance of the class
        self.first=first #instance variable
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
        employee.numofemps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) #we can use class here also.

emp1=employee('shubham','yadav',50000) #the emp1 is instance of the class
emp2=employee('dinesh','yadav',60000)  #the emp2 is instance of the class

emp1.raise_amt=1.05
#print(emp1.pay)
#emp1.apply_raise()
#print(emp1.pay)
#print(employee.numofemps)
print(employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
