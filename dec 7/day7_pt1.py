file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()


rule_dict = {}

for line in lines:
    x = line.split(" contain ")
    key = x[0]
    if "bags" in key:
        key = key[:-5]
    else:
        key = key[:-4]
        
    val = x[1]
    newbaglist = []
    x = val[:-1].split(", ")
    if (x[0] == "no other bags"):
        pass
    else:
        for bag in x:
            if "bags" in bag:
                newbaglist.append(bag[bag.index(" ")+1 : -5 ])
            else:
                newbaglist.append(bag[bag.index(" ")+1 : -4 ])
    rule_dict[key] = newbaglist


list_of_branches = []
for key in rule_dict:
    val = rule_dict.get(key)
    list_to_check = []
    for next_step in val:
        list_to_check.append([key,next_step])
    while len(list_to_check) != 0:
        cur_branch = list_to_check.pop(0)
        item = cur_branch[-1]
        if (item in rule_dict) and (rule_dict.get(item) != []) and (item != "shiny gold"):
            y = rule_dict.get(item)
            for next_step in y:                    
                x = cur_branch[:]
                x.append(next_step)
                if next_step == "shiny gold":
                    list_to_check = []
                    list_of_branches.append(x)
                elif (x not in list_to_check) and (x not in list_of_branches):
                    list_to_check.append(x)
                
        else:
            list_of_branches.append(cur_branch)

outcome_colors=[]
for i in list_of_branches:
    if (i[0] != "shiny gold") and ("shiny gold" in i) and (i[0] not in outcome_colors):
        outcome_colors.append(i[0])

print("ANS", len(outcome_colors))
        
    

