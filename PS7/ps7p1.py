class Employee:
    def __init__(self, first: str, last: str, salary: int):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
        self.email = f"{first}.{last}@company.com".lower()

    def Fullname(self) -> str:
        return f"{self.first} {self.last}"

    def Bonus(self, rate: float) -> float:
        return rate * self.salary

employee = Employee("Steve", "Rogers", 50000)
bonus = employee.Bonus(0.10)
print (f"${bonus:.2f}")