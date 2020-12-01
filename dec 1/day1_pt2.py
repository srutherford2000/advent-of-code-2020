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
        for r in lines:
            s =int(float(r))
            #print(a, float(a), int(float(a)))
            if (j != b) and (j != s) and (s != b) and ( j + b + s == 2020 ):
                print(j, b, s, s*j*b)

