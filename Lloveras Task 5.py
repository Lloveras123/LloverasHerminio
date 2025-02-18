class crocodile:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increased by {amount}. New salary: {self.salary}")

    def display_employee(self):
        print(f"Crocodile: {self.name}, Position: {self.position}, Salary: {self.salary}")

# Create an employee and give them a raise
employee = crocodile("Ronnel Cabia-an", "Brgy. Captain", 10000)
employee.display_employee()
employee.give_raise(1500)
employee.display_employee()
