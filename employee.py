
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

    # Define a method to calculate total pay
    def get_pay(self):
        if self.contract_type == "salary":
            pay = self.monthly_salary
            if self.bonus_commission is not None:
                pay += self.bonus_commission
        elif self.contract_type == "hourly":
            pay = self.hourly_wage * self.hours_worked
            if self.bonus_commission is not None:
                pay += self.bonus_commission
        if self.contract_commission is not None:
            commission = self.contract_commission * self.contracts_landed
            pay += commission
        return pay

    # Define __str__ method to explain pay calculation
    def __str__(self):
        pay_details = f"{self.name} works on a"
        if self.contract_type == "salary":
            pay_details += f" monthly salary of {self.monthly_salary}"
            if self.bonus_commission is not None:
                pay_details += f" and receives a bonus commission of {self.bonus_commission}"
        elif self.contract_type == "hourly":
            pay_details += f" contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
            if self.bonus_commission is not None:
                pay_details += f" and receives a bonus commission of {self.bonus_commission}"
        if self.contract_commission is not None:
            pay_details += f" and receives a commission for {self.contracts_landed} contract(s) at {self.contract_commission}/contract"
        total_pay = self.get_pay()
        return f"{pay_details}. Their total pay is {total_pay}."
