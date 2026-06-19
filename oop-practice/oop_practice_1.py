#  OOP Practice 1: basic classes 
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
         #We can use both self.raise_amount and Employee.raise_amount but only raise_amount won't work because we need to specify the class

emp_1=Employee('Vishal','Prajapati',80000) #emp_1 is an instance variable 
emp_2=Employee('Sujeet','Behera',60000)
print(emp_1.email)   #prints the email of the employee
print(emp_2.full_name()) 
print(Employee.full_name(emp_2))
#Both of these work same because emp_2.full_name() is interpreted same as Employee.full_name(emp_2) that's why we need to give self as a parameter in full_name()
print(emp_1.raise_amount)
print(Employee.raise_amount)
"""emp_1.raise_amount works becuase first it checks if the instance i.e emp_1 
   contains that attribute and if it doesn't it checks and expresses the class's attribute. 
   We can also print the namespace of emp_1 using __dict__ which shows that their is no attribute raise_amount in that list"""
print(emp_1.__dict__)
print(Employee.__dict__) #We can see this contains raise_amount
emp_1.raise_amount=1.10 
#This only change emp_1 raise amount but Employee.raise_amount would have changed it for all employees and this also create raise_amount instance in emp_1
print(emp_1.__dict__) #We can see raise amount in this
print(Employee.no_of_employees)