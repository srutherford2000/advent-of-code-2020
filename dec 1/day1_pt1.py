file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

for i in lines:
    j =int(float(i))
    #print(i, float(i),int(float(i)))
    for a in lines:
        b =int(float(a))
        #print(a, float(a), int(float(a)))
        if (j != b) and ( j + b == 2020 ):
            print(j, b, j*b)
