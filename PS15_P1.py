# Base Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, bonus_rate):
        bonus = bonus_rate * self.salary
        return bonus

# Derived Manager class
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)  # Call the parent class's constructor

    def long_term_bonus(self):
        return 0.40 * self.salary  # 40% of the salary

# Example program to test the Manager class
manager = Manager("Bezos", 80000)

# Calculate regular bonus (e.g., 10% bonus)
bonus_rate = 0.1
regular_bonus = manager.calculate_bonus(bonus_rate)
print(f"Manager {manager.name} has a regular bonus of: ${regular_bonus:.2f}")

# Calculate long-term bonus (40% of salary)
lt_bonus = manager.long_term_bonus()
print(f"Manager {manager.name} has a long-term bonus of: ${lt_bonus:.2f}")
