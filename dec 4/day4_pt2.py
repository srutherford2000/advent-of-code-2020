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
valid_eye_color = ["amb","blu","brn","gry","grn","hzl","oth"]
valid_hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for passport in passports:
    listoffields = passport.split()
    list_of_types = []
    for a_field in listoffields:
        a = a_field.split(':')
        list_of_types.append(a[0])
    if (len(listoffields) == 7) and ("cid" not in list_of_types):
        listoffields.append("cid:123")
    if len(listoffields) == 8 :
        listoffields.sort()
        #print(listoffields)
        ##parse data for birth year
        byr = listoffields[0]
        byr_split = byr.split(":")
        byr_data = int(float(byr_split[1]))     
        #print("byr", byr_data)
        if (byr_data>= 1920) and (byr_data <=2002):##correct birthday
            ##parse data for issue year
            iyr = listoffields[6]
            iyr_split = iyr.split(":")
            iyr_data = int(float(iyr_split[1]))
            #print("iyr", iyr_data)
            if (iyr_data>= 2010) and (iyr_data <=2020): ###correct issue year
                ##parse data for expiration year
                eyr = listoffields[3]
                eyr_split = eyr.split(":")
                eyr_data = int(float(eyr_split[1]))
                #print("eyr", eyr_data)
                if (eyr_data>= 2020) and (eyr_data <=2030): ###correct expiration year                   
                    #parse data for eye color
                    ecl = listoffields[2]    
                    ecl_split = ecl.split(":")
                    ecl_data = ecl_split[1]    
                    #print("ecl", ecl_data)
                    if ecl_data in valid_eye_color: ###correct eye color
                        #parse passport id num  
                        pid = listoffields[7]
                        pid_split = pid.split(":")
                        pid_data = pid_split[1]
                        #print("pid", pid_data)
                        if pid_data.isnumeric() and len(pid_data) == 9: ###correct eye color
                            #parse hair color data
                            hcl = listoffields[4]
                            hcl_split = hcl.split(":")
                            hcl_data = hcl_split[1]
                            #print("hcl", hcl_data)
                            hcl_is_valid = True
                            if (len(hcl_data) == 7):
                                if ( hcl_data[0] == '#'):
                                    for char in hcl_data[1:]:
                                        if char not in valid_hex_chars:
                                            hcl_is_valid = False
                                            break
                                else:
                                    hcl_is_valid = False
                            else:
                                hcl_is_valid = False
                            if hcl_is_valid:
                                ##parse height data
                                hgt = listoffields[5]
                                hgt_split = hgt.split(":")
                                hgt_data = hgt_split[1]
                                #print("hgt", hgt_data)
                                if ( "cm" in hgt_data) or ("in" in hgt_data):
                                    hgt_num = int(float(hgt_data[:-2]))
                                    hgt_unit = hgt_data[-2:]
                                    if hgt_unit == "cm":
                                        if (hgt_num >= 150) and (hgt_num <= 193):
                                            valid += 1
                                            print(listoffields)
                                    else:
                                        if (hgt_num >= 59) and (hgt_num <= 76):
                                            valid += 1
                                            
print("Valid Passport num is:",valid)

        
        
