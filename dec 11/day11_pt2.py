import copy
file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()


def check_surrounding_area(x,y, lis):
    num = 0
    change_list = [-1,0,1]
    ##this does the diagnoals where
    for i in change_list:
        for j in change_list:
            if (i== 0) and (j ==0):
                pass
            else:
                new_x = x + j
                new_y = y + i
                if (new_x >= 0) and (new_x <len(lis[0])) and (new_y >= 0) and (new_y <len(lis)):
                    val = lis[new_y][new_x]
                    while val == ".":
                        new_x += j
                        new_y += i
                        if (new_x >= 0) and (new_x <len(lis[0])) and (new_y >= 0) and (new_y <len(lis)):
                            val = lis[new_y][new_x]
                        else:
                            break
                    if val == "#": ##means we broke out of the while
                        num += 1
    return num

old_list = copy.deepcopy(lines)
new_list = copy.deepcopy(old_list)
check = True

while (check):
    for y_val in range(len(old_list)):
        for x_val in range(len(old_list[0])):
            num_surrounding = check_surrounding_area(x_val,y_val,old_list)
            val = old_list[y_val][x_val]
            line = new_list[y_val]
            if (num_surrounding >= 5) and (val == "#"):
                new_line = line[:x_val] + "L" + line[x_val+1:]
                new_list[y_val]= new_line
            elif (num_surrounding == 0) and (val == "L"):
                new_line = line[:x_val] + "#" + line[x_val+1:]
                new_list[y_val]= new_line
    #for line in new_list:
     #   print(line)
    #print()
    if (new_list == old_list):
        check = False
    else:
        old_list = copy.deepcopy(new_list)
            

full_count = 0
for line in new_list:
    for seat in line:
        if seat == "#":
            full_count += 1

print("ANS is :", full_count)
    
