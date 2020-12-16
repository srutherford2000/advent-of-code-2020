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
for rule in rule_lines:
    split_em = rule.split()
    new_list = [split_em[-1]]
    new_list.append(split_em[-3])
    for nums in new_list:
        split_em_2 = nums.split("-")
        for ind in range(2):
            x = split_em_2[ind]
            split_em_2[ind] = int(float(x))
        for i in range (split_em_2[0], split_em_2[1]+1):
            if i not in valid_numbers:
                valid_numbers.append(i)


##parse nearby tickets
nearby_tickets.pop(0)
invalid_ticket = []
for ticket in nearby_tickets:
    list_of_ticket = ticket.split(",")
    for num in list_of_ticket:
        num = int(float(num))
        if num not in valid_numbers:
            invalid_ticket.append(num)
            break
    
print("ANS is:", sum(invalid_ticket))
    

in_file.close()
