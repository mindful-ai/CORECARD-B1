class employee:

    # Class variable
    empCount = 0

    # Data
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.tax = 0
        employee.empCount += 1

    # Functions

    def printinfo(self):
        print("-"*50)
        print('NAME    : ', self.name)
        print('AGE     : ', self.age)
        print("-"*50)
        print("GROSS SALARY : ", self.salary)
        print("TAX AMOUNT   : ", self.tax)
        print("-"*50)
        print("NET SALARY   : ", self.salary - self.tax)
        print("SELF  ---> ", self)
        print("-"*50 + '--- End of Report')


    def calctax(self, pct):
        self.tax = self.salary * (pct/100)

    def calchike(self, hikepct):
        pass

class employee_child(employee):
    pass

class employee_child2(employee):
    
    # Data
    def __init__(self, name, age, salary, phone, addr):
        super().__init__(name, age, salary)
        self.phone = phone
        self.addr = addr

    # Functions (Extra functions and redefined functions)
    # Note that all functions and data of parent (employee class) is available here


    def printinfo(self):
        super().printinfo()
        print("PHONE  : ", self.phone)
        print('ADDRESS  :', self.addr)

    def addbonus(self, amount):
        self.salary = self.salary + amount




# --------------------------------- Application developer

ep = employee("Raj", 27, 100000)
e1 = employee_child("Raj", 27, 100000)
print(e1)
e1.printinfo()


e1.calctax(17)
e1.printinfo()

# -------------------------------------------------------------- after inheritance


e = employee_child2("Ram", 40, 1000000, '+91-9872349834', 'Bangalore, India')
e.printinfo()
e.calctax(15)
e.printinfo()
e.addbonus(200000)
e.calctax(15)
e.printinfo()

# --------------------------------------------------- polymorphism

#x = ep
x = e
x.printinfo()

