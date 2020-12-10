file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(int(float(line.strip())))

in_file.close()

lines.sort()

num_of_threes = 1 #accounts for the one at the end
num_of_ones = 0

last_num = 0

for num in lines:
    dif = num - last_num
    if (dif == 3):
        num_of_threes += 1
    elif (dif ==1):
        num_of_ones += 1
    last_num = num

print("ANS is:", num_of_threes * num_of_ones)
