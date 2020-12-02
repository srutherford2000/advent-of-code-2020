file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

list_of_split_lines = []

for line in lines:
    split_line = line.split()
    list_of_split_lines. append(split_line)

num_of_valid = 0
for li in list_of_split_lines:
    let = li[1][0]
    num_split = li[0].split('-')
    lower_num = int(float(num_split[0]))
    upper_num = int(float(num_split[1]))
    password = li[2]
    if (password.count(let) <= upper_num ) and (password.count(let) >= lower_num ):
        num_of_valid += 1
print(num_of_valid)
    
    
