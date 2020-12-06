file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

linesTogether = []

#combine multiple lines to one input string"
combine = []
for line in lines:
    if (line == ""):
        linesTogether.append(combine)
        combine = []
    else:
        combine.append(line)
linesTogether.append(combine)

#print(linesTogether)

alphabet = "abcdefghijklmnopqrstuvwxyz"

sum_of_counts = 0
for group in linesTogether:
    count = 0
    for let in alphabet:
        all_have_let = True
        for person in group:
            if (let not in person):
                all_have_let = False
                break
        if all_have_let:
            count += 1
            #print(let,group)
    sum_of_counts += count

print("ANS is:",sum_of_counts)
