
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

    def calculate_base_pay(self):
        if self.contract_type == "salary":
            return self.monthly_salary
        elif self.contract_type == "hourly":
            return self.hourly_wage * self.hours_worked
        return 0

    def calculate_commission(self):
        commission = 0
        if self.bonus_commission is not None:
            commission += self.bonus_commission
        if self.contract_commission is not None and self.contracts_landed is not None:
            commission += self.contract_commission * self.contracts_landed
        return commission

    def get_pay(self):
        return self.calculate_base_pay() + self.calculate_commission()

    def __str__(self):
        pay_details = f"{self.name} works on a "
        if self.contract_type == "salary":
            pay_details += f"monthly salary of {self.monthly_salary}"
        elif self.contract_type == "hourly":
            pay_details += f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
        
        if self.bonus_commission is not None:
            pay_details += f" and receives a bonus commission of {self.bonus_commission}"
        if self.contract_commission is not None:
            pay_details += f" and receives a commission for {self.contracts_landed} contract(s) at {self.contract_commission}/contract"
        
        total_pay = self.get_pay()
        return f"{pay_details}. Their total pay is {total_pay}."

# Examples of constructing employee objects
billie = Employee(name="Billie", contract_type="salary", monthly_salary=4000)
charlie = Employee(name="Charlie", contract_type="hourly", hourly_wage=25, hours_worked=100)
renee = Employee(name="Renee", contract_type="salary", monthly_salary=3000, contract_commission=200, contracts_landed=4)
jan = Employee(name="Jan", contract_type="hourly", hourly_wage=25, hours_worked=150, contract_commission=220, contracts_landed=3)
robbie = Employee(name="Robbie", contract_type="salary", monthly_salary=2000, bonus_commission=1500)
ariel = Employee(name="Ariel", contract_type="hourly", hourly_wage=30, hours_worked=120, bonus_commission=600)
