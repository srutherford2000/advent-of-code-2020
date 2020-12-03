file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

num_repeats_nessisary = (int(len(lines) / len(lines[0])) + 1)*3

updated_lines= []

for line in lines:
    line *= num_repeats_nessisary
    updated_lines.append(line)

x = 0
num_trees_hit = 0

for y in range(0,len(lines)):
    #print(y,x)
    if (updated_lines[y][x] == '#'):
        num_trees_hit += 1
    x += 3

print(num_trees_hit)
