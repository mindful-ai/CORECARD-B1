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

# --------------------------------- Application developer

e1 = employee("Raj", 27, 100000)
print(e1)
e1.printinfo()


e1.calctax(17)
e1.printinfo()

# Assignment: Make appropriate changes in the class
e1.calchike(18)
e1.printinfo()