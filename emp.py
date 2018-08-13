from abc import ABCMeta, abstractmethod

class employee(metaclass=ABCMeta):
    no_emp = 0
    
    @abstractmethod
    def accept():
        """accept"""

    @abstractmethod
    def display():
        """display"""

    @abstractmethod
    def no_employee():
        """Display no of employee"""

class Developer(employee):
    def __init__(self,eid):
        self.eid = eid
        employee.no_emp +=1

    def accept(self):
        self.name = input("Enter the employee name")
        self.salary = float(input("Enter the salary"))

    def display(self):
        print("Employee eid : "+str(self.eid))
        print("Employee ename : "+self.name)
        print("Employee salary : "+str(self.salary))

    def no_employee(self):
        print("The no of employee"+str(employee.no_emp))


class Manager(employee):
    def __init__(self,eid):
        self.eid = eid
        employee.no_emp +=1


    def accept(self):
        self.name = input("Enter the Manager name")
        self.salary = float(input("Enter the salary"))
        self.dept = input("Enter the department")

    def display(self):
        print("Manager mid : "+str(self.eid))
        print("Manager mname : "+self.name)
        print("Manager salary : "+str(self.salary))
        print("Manager Department : "+self.dept)

    def no_employee(self):
        print("The no of employee"+str(employee.no_emp))





emp_1 = Developer(1)
emp_1.accept()
emp_1.display()
man_1 = Manager(2)
man_1.accept()
man_1.display()
man_1.no_employee()
