
def genReport(dd):
    dottedline = '-'*70
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:3}'
    print('CLASS REPORT')
    print(dottedline)
    print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
    print(dottedline)
    for regid in dd.keys():
        name = dd[regid]['name']
        age  = dd[regid]['age']
        regid = dd[regid]['regid']
        phy = dd[regid]['phy']
        chem = dd[regid]['chem']
        math = dd[regid]['math']
        bio = dd[regid]['bio']
        avg = dd[regid]['avg']
        rank = dd[regid]['rank']
        print(template.format( regid, name, age,phy, chem, math, bio, avg, rank))
    print(dottedline)

# [LAB] Complete the function definition
# It should write the report to the file specified by "path"
def write2file(dd, path):
    pass

# Read the csv file as a text file


print(content)
print('-'*60 + ' > First Step')



# ------------------------ csv file is read and its content is available for further processing

# Read the coloums --> name,age,regid,phy,chem,math,bio,avg,rank
# Read a row --> Vijay,14,HPE001,99,98,97,96,0,0
# Construct a dictionary out of the column and the row
# Add that dictionary to the main dictionry that represents the class
# Repeat this process for all the entries in the csv file



print(classdict)
print('-'*60 + ' > Second Step')

# ------------------------- csv data is in the form of a dictionary

# Access the dictionary iteratively and calculate the average marks and
# update in the dictionary

# [LAB] Write code to calculate the average for all the students

print(classdict)
print('-'*60 + ' > Third Step')

# ------------------------- dictionary updated with average data

# Calculate the rank
# collect all the averages -> into a list
# arrange the averages in descending order
# iterate the entire dictionary and update the rank based on the descending
# order of averages

# [LAB] Write code to calculate the rank for all the students

print(classdict)
print('-'*60 + ' > Fourth Step')   



# ------------------------- dictionary updated with rank data

# Re-write the csv file

path = r"students_completed.csv"


f.close()

# ------------------------- resultant csv file is now ready with averages and ranks updated

genReport(classdict)
write2file(classdict, r"report2.txt")