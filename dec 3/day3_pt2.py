file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

def find_trees( right, down):
    num_repeats_nessisary = (int(len(lines) / len(lines[0])) + 1)*right

    updated_lines= []

    for line in lines:
        line *= num_repeats_nessisary
        updated_lines.append(line)

    x = 0
    num_trees_hit = 0

    for y in range(0,len(lines),down):
        #print(y,x)
        if (updated_lines[y][x] == '#'):
            num_trees_hit += 1
        x += right

    return num_trees_hit


a = find_trees(1,1)
b = find_trees(3,1)
c = find_trees(5,1)
d = find_trees(7,1)
e = find_trees(1,2)

print(a*b*c*d*e)
