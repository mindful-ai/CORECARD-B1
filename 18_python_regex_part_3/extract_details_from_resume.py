import re
EOF = ''
# Read the file as a text

f = open( "resume.txt", "r" )
content = f.read()
f.close()
# Patterns
# use regex101.org for composing regular expressions
jobid = r"#\d{6}"
email = r"(\w+\.)*\w+@\w+\.\w+"
phone = r"\d{3}-\d{3}-\d{4}"
linkedin = r""
name = r"(Sincerely,)\s(?P<Name>\w+\s\w*)"
ipaddr = r""

# Apply the patterns and store what ever is extracted



m = re.search(jobid, content)
if m:
    print('JOBID     : ', m.group())

m = re.search(email, content)
if m:
    print('EMAIL     : ', m.group())

m = re.search(phone, content)
if m:
    print('PHONE     : ', m.group())

m = re.search(linkedin, content)
if m:
    print('LINKEDIN  : ', m.group())

m = re.search(name, content)
if m:
    print('NAME      : ', m.groupdict()['Name'])

m = re.search(ipaddr, content)
if m:
    print('IP        : ', m.group())