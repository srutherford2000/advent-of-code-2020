file_name=input('enter a file name')
in_file=open(file_name)
lines=[]

batch = []

for line in in_file:
    line = line.strip()
    if line != "":
        batch.append(line)
    else:
        lines.append(batch)
        batch = []
    
lines.append(batch)

rule_lines = lines[0]
my_tick_lines = lines[1]
nearby_tickets = lines[2]

##parse the rule lines
valid_numbers = []
ranges = []
for rule in rule_lines:
    split_em = rule.split()
    new_list = [split_em[-1]]
    new_list.append(split_em[-3])
    y = []
    for nums in new_list:
        split_em_2 = nums.split("-")
        for ind in range(2):
            x = split_em_2[ind]
            split_em_2[ind] = int(float(x))
        for i in range (split_em_2[0], split_em_2[1]+1):
            y.append(i)
            if i not in valid_numbers:
                valid_numbers.append(i)
    ranges.append(y)

##parse my ticket lines
my_ticket = my_tick_lines[1].split(",")
for i, num in enumerate(my_ticket):
    my_ticket[i] = int(float(num))


##parse nearby tickets
nearby_tickets.pop(0)
invalid_ticket = []
for ind, ticket in enumerate(nearby_tickets):
    list_of_ticket = ticket.split(",")
    for i, num in enumerate(list_of_ticket):
        list_of_ticket[i] = int(float(num))
    nearby_tickets[ind] = list_of_ticket
    for num in list_of_ticket:
        if num not in valid_numbers:
            invalid_ticket.append(list_of_ticket)
            break

##get valid tickets
valid_tickets=[]
for ticket in nearby_tickets:
    if ticket not in invalid_ticket:
        valid_tickets.append(ticket)

dic_nums_in_row = {}

for i in range(len(my_ticket)):
    dic_nums_in_row[i] = [my_ticket[i]]
    for tic in valid_tickets:
        dic_nums_in_row[i].append(tic[i])

possible_fields = {}
for i in range(len(ranges)):
    possible_fields[i] = []
for thing in dic_nums_in_row.values():
    for ind,r in enumerate(ranges):
        for i, num in enumerate(thing):
            if num not in r:
                break
            elif (i == (len(thing)-1)):
                possible_fields[ind].append(thing)


def check_every_val_in_dic_is_empty(diction):
    for val in diction.values():
        if len(val)!= 0:
            return False
    return True


current_status = False

final_dict = {}

while current_status == False:
    for key, value in possible_fields.items():
        if len(value) == 1:
            final_dict[key] = value[0][0]
            x = value[0]
            for value1 in possible_fields.values():
                if x in value1:
                    where = value1.index(x)
                    value1.pop(where)
    current_status = check_every_val_in_dic_is_empty(possible_fields)

print(final_dict)
##note the 0,1,2,3,4,5 numbers corespond to the desired fields in the problem
print("ANS is:", final_dict[0] * final_dict[1] * final_dict[2] * final_dict[3] * final_dict[4] * final_dict[5])
in_file.close()
