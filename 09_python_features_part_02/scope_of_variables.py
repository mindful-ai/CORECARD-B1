a = 10 # Global Variable

def myfunction():
    print('(myfunction) The value of a is :', a)

def myfunction2():
    a = 5 # Local variable
    print('(myfunction2) The value of a is :', a)

def myfunction1():
    def myfunction():
        print('(myfunction3.myfunction) The value of a is :', a)
    myfunction()

def myfunction1a():
    a = 5 # non-local variable
    def myfunction():
        print('(myfunction3.myfunction) The value of a is :', a)
    myfunction()

def myfunction1b():
    a = 5 # non-local variable
    def myfunction():
        a = 1 # local variable
        print('(myfunction3.myfunction) The value of a is :', a)
    myfunction()

def myfunction1c():
    a = 5 # non-local variable
    def myfunction():
        global a
        print('(myfunction3.myfunction) The value of a is :', a)
    myfunction()

if __name__ == "__main__":

    myfunction()
    myfunction2()
    myfunction1()
    myfunction1a()
    myfunction1b()
    myfunction1c()