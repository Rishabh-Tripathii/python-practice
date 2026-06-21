# OOP Practice 3: dunder methods (__str__, __repr__)

class Employee:
    no_of_employees=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '_' + last + '@company.com'
        Employee.no_of_employees+=1

    def full_name(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
