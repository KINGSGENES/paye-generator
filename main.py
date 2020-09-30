# this is a project to calculate the taxes and ssnit payments for individual employees
from tax_calcs import paye, ssnit, ssnit_tier2


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def ssnit_payable(self):
        return ssnit(self.salary)

    def ssnit_tier2(self):
        return ssnit_tier2(self.salary)

    def paye_payable(self):
        return paye(self.salary)


kwadwo = Employee('Kwadwo', 36, 1000)

print(kwadwo.paye_payable())
