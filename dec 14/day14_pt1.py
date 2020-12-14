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
        if mask_let == "1" and bin_num_let != "1":
            let_in_bin_final = let_in_bin_final[:i] + "1" + let_in_bin_final[i+1:]
        elif mask_let == "0" and bin_num_let != "0":
            let_in_bin_final = let_in_bin_final[:i] + "0" + let_in_bin_final[i+1:]
    final_int = int(let_in_bin_final, 2)
    return final_int

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
        bin_num = int(data_as_list[1])
        final_num = find_mask_comparison(mask, bin_num)
        dic[mem_loc] = final_num

final_ans=0

for num in dic.values():
    final_ans += num

print("ANS is:", final_ans)
        
    
    
    
