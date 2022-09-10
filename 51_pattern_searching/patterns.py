from datetime import datetime
def pattern(string, substr):
    length = len(substr)
    start = 0
    end = length
    '''
    print(start, end)
    if(string[start:end] == substr):
        return substr
    else:
        return False
    '''
    indeces = []
    while end <= len(string):
        if(string[start:end] == substr):
            indeces.append((start, end))
        start += 1
        end += 1
    return indeces


    

# ----------------------------------------


string = 'FFBSDDAABDCFFBSDDHTNELLAKKKDFFBSDDHTNELLAFFBSDDHTNELLAFFBSDD'
substr = 'FFBSDD'
result = pattern(string, substr)
print(result)

string = 'mississippi'
substr = 'ss'
print(pattern(string, substr))

string = 'AAAAAAAAAAAAAAAAAAA'
substr = 'AAA'
print(pattern(string, substr))