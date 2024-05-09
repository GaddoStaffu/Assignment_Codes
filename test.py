# class
class Employee:
    # methods (functions inside a class)
    def __init__(self, name, age, position, address):
        # class instance attributes (variables inside a class)
        self.name = name
        self.age = age
        self.position = position
        self.address = address


    def description(self):
        return f'I am {self.name}. I am {self.age}. I live in {self.address}'
        
        
# Instances / Object
employee1 = Employee('Person1', 34, 'Manager', 'Address1')
employee2 = Employee('Person2', 30, 'Assistant Manager', 'Address2')
employee3 = Employee('Person3', 25, 'Cashier', 'Address3')

print(employee1.description())
print(employee2.description())
print(employee3.description())

# print(employee1.name)
# print(employee2.name)
# print(employee3.name)

# employee1 = ['Person1', 34, 'Manager', 'Address1']
# employee2 = ['Person2', 30, 'Assistant Manager', 'Address2']
# employee3 = ['Person3', 'Cashier', 'Address3']