class employee:
    raiseamt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    def fullname(self):
        return '{} {}' .format(self.first,self.last)

    def applyraise(self):
        self.pay = int(self.pay * self.raiseamt)


dev1 = employee('shubham','yadav',50000)
dev2 = employee('dinesh', 'yadav',60000)



