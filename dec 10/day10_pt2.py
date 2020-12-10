file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(int(float(line.strip())))

in_file.close()
lines.append(0) #change to 75 when using the second half

lines.sort()

def path(cur_ind):
    val = lines[cur_ind]
    i = cur_ind+1
    next_steps=[]
    next_steps_vals = []
    paths = 0
    while (i<len(lines) )and (i-cur_ind <=3):
        next_val = lines[i]
        if next_val - val <= 3:
            next_steps.append(i)
            next_steps_vals.append(next_val)
        else: 
           break
        i += 1
    if (cur_ind >= len(lines)) or next_steps_vals == []:
        return 1
    else:
        for thing in next_steps:
            x = path(thing)
            paths += x
        return paths
    


y = path(0)
print(y)
