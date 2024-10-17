


class Employee:

    def __init__(self,name,age,salary):

        self.name=name

        self.age=age

        self.salary=salary

    def get_salary(self):

        return self.salary
# class method

    @classmethod
    def get_company(self):

        return "luminar"

emp1=Employee("hari",25,567890)
emp2=Employee("vipin",25,567890)
emp3=Employee("subin",25,567890)
print(Employee.get_company())