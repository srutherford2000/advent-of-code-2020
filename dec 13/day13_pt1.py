file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

goal = int(float(lines[0]))

possible = lines[1].split(",")

good_list= []
for thing in possible:
    if thing != "x":
        good_list.append(int(float(thing)))

list_of_possible_good_times = []
for ind in range(len(good_list)):
    num = good_list[ind]
    lowest_val = 0
    while lowest_val <= goal:
        lowest_val += num
    list_of_possible_good_times.append(lowest_val)

way_to_go = min(list_of_possible_good_times)
ind_of_way_to_go = list_of_possible_good_times.index(way_to_go)

ans = (good_list[ind_of_way_to_go]) * (way_to_go - goal)

print("ANS is:",ans)
