file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

linesTogether = []

#combine multiple lines to one input string"
combine = ""
for line in lines:
    if (line == ""):
        linesTogether.append(combine)
        combine = ""
    else:
        combine += line 
linesTogether.append(combine)

alphabet = "abcdefghijklmnopqrstuvwxyz"

sum_of_counts = 0
for i in linesTogether:
    count = 0
    lettersFound = []
    for let in alphabet:
        if (let not in lettersFound) and (let in i):
            count += 1
            lettersFound.append(let)
    sum_of_counts += count

print("ANS is:",sum_of_counts)

