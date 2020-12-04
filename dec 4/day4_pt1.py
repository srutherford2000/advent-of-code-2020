file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

passports = []

#combine the passpors read in multiple lines to one input string"
combine = ""
for line in lines:
    if (line == ""):
        passports.append(combine[:-1])
        combine = ""
    else:
        combine = combine + line + " "
passports.append(combine[:-1])

#check to see if they have 8 fields or are just missing cid
valid = 0
for passport in passports:
    listoffields = passport.split()
    list_of_types = []
    for a_field in listoffields:
        a = a_field.split(':')
        list_of_types.append(a[0])
    if len(listoffields) == 8:
        valid += 1
    elif (len(listoffields) == 7) and ("cid" not in list_of_types):
        valid += 1

print(valid)
