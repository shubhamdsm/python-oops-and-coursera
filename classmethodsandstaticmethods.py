class employee:

    numofemps=0
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
        employee.numofemps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @classmethod
    def set_raise(cls,amount):
         cls.raise_amt= amount

    @staticmethod
    def isworkday(day):
        if day.weekday() ==5 or day.weekday() ==6:
            return False
        return True




emp1=employee('shubham','yadav',50000)
emp2=employee('dinesh','yadav',60000)

import datetime
my_date = datetime.date(2016,7,11)
print(employee.isworkday(my_date))



#emp_str_1='tarun-kaushal-90000'
#newemp=employee.from_string(emp_str_1)
#print(newemp.first)
#emp1.set_raise(1.05)
#print(employee.raise_amt)


#emp_str_2='subham-kumar-50000'
#emp_str_3='saurav-yadav-60000'
#emp_str_4='vikash-kumar-70000'

