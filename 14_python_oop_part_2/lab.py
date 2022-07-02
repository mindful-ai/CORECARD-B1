class student:

    def __init__(self, studname, studage, studclass):
        # name, age, class, marks (dict of subjects), avg, rank
        pass

    def printreport(self):
        pass

    def setmarks(self, sub, marks):
        # phy, chem, math, bio
        # Automatically call calcaverage -> self.calcaverage()
        pass

    def calcaverage(self):
        # Automatically call when a setmarks is called
        pass

    def setrank(self, rank):
        pass

class extstudent(student):

    def __init__(self, studname, studage, studclass, hobbies, address, languages):
        # hobbies and languages are lists
        pass

    def printreport(self):
        pass

    def changeinfo(self, info, value):
        # info -> name/age/class
        # changeinfo('name', 'Kiran')
        pass

    def addhobby(self, hobby):
        pass

    def addlanguage(self, lang):
        pass

    def removehobby(self, hobby):
        pass

    def removelang(self, lang):
        pass

# -----------------------------------------------------------------------------


s = student("Anil", 10, 4)
es = extstudent("Anil", 10, 4, [], 'Indore, India', ['Hindi', 'English'])
es.printreport()
es.addhobby('cricket')
es.printreport()


# Do more tests
# Test every function