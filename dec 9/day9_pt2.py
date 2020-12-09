file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(int(float(line.strip())))

in_file.close()

search_val = 21806024 #found in part 1


current_contiguous_set = []

for num in lines:
    current_contiguous_set.append(num)
    while sum(current_contiguous_set) > search_val:
        current_contiguous_set = current_contiguous_set[1:]
    if sum(current_contiguous_set) == search_val:
        print(current_contiguous_set, "yay")
        break

minimum = min(current_contiguous_set)
maximum = max(current_contiguous_set)

print("The ANS is:", minimum + maximum)
