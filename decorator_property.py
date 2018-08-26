class Employee:
    raise_amount = 1.04
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay= emp_str.split('-')
        return  cls(first, last, int(pay))

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, selflast = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print("Name Deleted")
        self.first = None
        self.last = None


emp_str_1 = 'John-Doe-70000'
emp_1 = Employee.from_string(emp_str_1)
print(emp_1.fullname)
emp_1.fullname = "Michal George"
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)
