file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()


lines_visited= []

current_instruction_ind = 0
accumulator = 0

while current_instruction_ind not in lines_visited:
    lines_visited.append(current_instruction_ind)
    cur_instruction = lines[current_instruction_ind]
    cur_instruction_split = cur_instruction.split()
    command = cur_instruction_split[0]
    num = int(float(cur_instruction_split[1]))
    if command=="nop":
        current_instruction_ind += 1
    elif command == "acc":
        accumulator += num
        current_instruction_ind += 1
    else: #its jump
        current_instruction_ind += num
        
    
print("current accumulator val:",accumulator)
