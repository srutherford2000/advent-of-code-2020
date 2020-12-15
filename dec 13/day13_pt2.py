file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()


possible = lines[1].split(",")

good_list= []
current_vals = []

for ind in range(len(possible)):
    thing = possible[ind]
    if thing != "x":
        good_list.append(int(float(thing)))
        current_vals.append(int(float(thing))-ind)

#good_list.sort()
#good_list.reverse()

#current_vals.sort()
#current_vals.reverse()
print(good_list)
print(current_vals)

all_equal = False

while all_equal == False:
    old = good_list[0]
    current_vals[0] += old
    for ind in range(1,len(good_list)):
        old = good_list[ind]
        #print(old)
        while (current_vals[ind] < current_vals[0]) :
            current_vals[ind] += old
    if current_vals.count(current_vals[0]) == len(current_vals) :
        all_equal = True
        print("ANS is:", current_vals)
    #else:
     #   print(current_vals)
    
        
        


