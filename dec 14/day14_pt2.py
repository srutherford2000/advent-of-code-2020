file_name=input('enter a file name')

in_file=open(file_name)

lines=[]
batch = []

for line in in_file:
    a = line.strip()
    if "mask" in a:
        lines.append(batch)
        batch = []
        batch.append(a)
    else:
        batch.append(a)
    
lines.append(batch)
lines = lines[1:]

in_file.close()


def find_mask_comparison(mask, num):
    let_in_bin = bin(num)[2:]
    more_zeros_needed = 36-len(let_in_bin)
    let_in_bin_final = more_zeros_needed*"0" + let_in_bin
    for i in range(len(mask)):
        mask_let = mask[i]
        bin_num_let = let_in_bin_final[i]
        if mask_let == "X":
            let_in_bin_final = let_in_bin_final[:i] + "X" + let_in_bin_final[i+1:]       
        elif mask_let == "1" and bin_num_let != "1":
            let_in_bin_final = let_in_bin_final[:i] + "1" + let_in_bin_final[i+1:]
    return let_in_bin_final

def work_through_combos(str_with_xs):
    s = set()
    count = str_with_xs.count("X")
    possible = [0,1]
    posibilities = [str_with_xs]
    finals=[]
    while len(posibilities)>0:
        current_val = posibilities.pop(0)
        ind = current_val.index("X")
        for num in possible:
            current_val = current_val[:ind] + str(num) + current_val[ind+1:]
            if "X" in current_val:
                posibilities.append(current_val)
            else:
                finals.append(current_val)
        #print(posibilities,finals)
    return finals
               
dic = {}

for batch in lines:
    mask_line = batch[0]
    mask_as_list = mask_line.split(" = ")
    mask = mask_as_list[1]
    for ind in range(1,len(batch)):
        data_line = batch[ind]
        data_as_list = data_line.split(" = ")
        mem_loc_part = data_as_list[0]
        mem_loc = mem_loc_part[mem_loc_part.index("[") + 1 : mem_loc_part.index("]")]
        final_num = int(data_as_list[1])
        num_str = find_mask_comparison(mask, int(mem_loc))
        #print(num_str)
        possibilites = work_through_combos(num_str)
        #print(possibilites)
        for poss in possibilites:
            mem_loc = int(poss,2)
            dic[mem_loc] = final_num

final_ans=0

for num in dic.values():
    final_ans += num

print("ANS is:", final_ans)
        
    
    
    
