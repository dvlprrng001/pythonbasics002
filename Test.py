class Employee:
    def __init__(self, name, date_of_birth) -> None:
        self.name = name
        self.date_of_birth = date_of_birth
    
    def Info(self):
        print(f''' Hello {self.name}  .. i am {self.date_of_birth} years old''')
    
emp01 = Employee("Shravya","10/10/2010")
emp01.Info()
