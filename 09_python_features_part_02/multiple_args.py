def average(a, b, c):
    return (a + b + c)/3

def average2(*targs):
    print(targs, type(targs))
    return sum(targs)/len(targs)

def average3(a, b, c, *targs):
    print(a, b, targs, type(targs))
    return sum(targs)/len(targs)

def myfunction(mesg="hello world"):  # default values to arguements
    print(mesg)

def myfunction2(name="Anil", mesg="Hello", n=10):  # keyword arguments
    print(mesg.upper(), ', ', name)

def myfunction3(a, b, c, *targs, **kargs): # The order should be maintained -> required args, targs, kargs
    print(a, b, c, targs, kargs)

if __name__ == '__main__':

    print(average(10, 20, 30))
    #print(average(10, 20, 30, 40))
    print(average2(10, 20, 30, 40, 50))
    print(average3(10, 20, 30, 40, 50))
    myfunction()
    myfunction("Python is an interesting computer programming language")
    myfunction2()
    myfunction2(name='Kiran')
    myfunction2(n=19, mesg='Hi!', name='Kiran') # The order here doesnot matter
    myfunction2('Kiran', 'Hi!', 14) # The order of arguments will matter
    #myfunction2('Kiran', 14, 'Hi!') # The order of arguments will matter, gives error

    myfunction3(10, 20, 30, 40, 50, 60, n1=100, n2=200, n3=400)
    myfunction3(10, 20, 30)
