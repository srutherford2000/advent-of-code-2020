file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(int(float(line.strip())))

in_file.close()

num_in_preamble = int(float(input("what is the num in the preamble")))


i = num_in_preamble

while i < len(lines):
    list_of_factors = lines[(i-num_in_preamble):i]
    num = lines[i]
    found = False
    for x in list_of_factors:
        if x> (num / 2):
            for y in list_of_factors:
                tot = x + y
                if tot == num and x!=y:
                    found = True
                    list_of_factors.append(num)
                    break
            if tot == num:
                break
    if found == False:
        print(num, "no match found")
        break
    i+=1

