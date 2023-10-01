
class Employee:
    def __init__(self, name, contract_type, monthly_salary=None, hourly_wage=None, hours_worked=None,
                 bonus_commission=None, contract_commission=None, contracts_landed=None):
        self.name = name
        self.contract_type = contract_type
        self.monthly_salary = monthly_salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus_commission = bonus_commission
        self.contract_commission = contract_commission
        self.contracts_landed = contracts_landed

    def get_pay(self):
        if self.contract_type == "salary" and self.bonus_commission is None and self.contract_commission is None:
            return self.monthly_salary
        elif self.contract_type == "hourly" and self.bonus_commission is None and self.contract_commission is None:
            return self.hourly_wage * self.hours_worked
        elif self.contract_type == "salary" and self.bonus_commission is not None:
            return self.monthly_salary + self.bonus_commission
        elif self.contract_type == "hourly" and self.bonus_commission is not None:
            return (self.hourly_wage * self.hours_worked) + self.bonus_commission
        elif self.contract_type == "salary" and self.contract_commission is not None:
            return self.monthly_salary + (self.contract_commission * self.contracts_landed)
        elif self.contract_type == "hourly" and self.contract_commission is not None:
            return (self.hourly_wage * self.hours_worked) + (self.contract_commission * self.contracts_landed)

    def __str__(self):
        pay_details = f"{self.name} works on a"
        if self.contract_type == "salary":
            pay_details += f" monthly salary of {self.monthly_salary}"
        elif self.contract_type == "hourly":
            pay_details += f" contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
        if self.bonus_commission is not None:
            pay_details += f" and receives a bonus commission of {self.bonus_commission}"
        if self.contract_commission is not None:
            pay_details += f" and receives a commission for {self.contracts_landed} contract(s) at {self.contract_commission}/contract"
        total_pay = self.get_pay()
        return f"{pay_details}. Their total pay is {total_pay}."



billie = Employee("Billie", "salary", monthly_salary=4000)
charlie = Employee("Charlie", "hourly", hourly_wage=25, hours_worked=100)
renee = Employee("Renee", "salary", monthly_salary=3000, contract_commission=200, contracts_landed=4)
jan = Employee("Jan", "hourly", hourly_wage=25, hours_worked=150, contract_commission=220, contracts_landed=3)
robbie = Employee("Robbie", "salary", monthly_salary=2000, bonus_commission=1500)
ariel = Employee("Ariel", "hourly", hourly_wage=30, hours_worked=120, bonus_commission=600)

# Test the get_pay() and __str__() methods
print(billie.get_pay())  # Should return 4000
print(str(billie))  # Should print the corresponding string

print(charlie.get_pay())  # Should return 2500
print(str(charlie))

print(renee.get_pay())  # Should return 3800
print(str(renee))

print(jan.get_pay())  # Should return 4410
print(str(jan))

print(robbie.get_pay())  # Should return 3500
print(str(robbie))

print(ariel.get_pay())  # Should return 4200
print(str(ariel))
