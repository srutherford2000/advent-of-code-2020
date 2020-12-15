def find_30000000th_Term(input_string):
    index_dic = {}
    occurance_dic = {}
    occurance_dic[0] = 0
    puzzle_input = input_string.split(",")
    for i in range(len(puzzle_input)):
        num = int(puzzle_input[i])
        puzzle_input[i] = num
        index_dic[num] = [i]
        if num not in occurance_dic:
            occurance_dic[num] = 1
        else:
            occurance_dic[num] += 1

    count =len(puzzle_input)

    while count < 30000000:
        if (count %10000 ==0 ):
            print(count)
        current_ind = count - 1
        last_num = puzzle_input[current_ind]
        if (occurance_dic[last_num] == 1):##means its the 1st occurance
            puzzle_input.append(0)
            if 0 not in index_dic:
                index_dic[0] = [count]
            else:
                a = index_dic[0]
                a.append(count)
                index_dic[0] = a
            occurance_dic[0]+=1         
        else:
            previous_occurance_ind = index_dic[last_num][-2]
            place_to_input  = current_ind - previous_occurance_ind
            if place_to_input not in occurance_dic:
                occurance_dic[place_to_input] = 1
                index_dic[place_to_input] = [count]
            else:
                occurance_dic[place_to_input] += 1
                a = index_dic[place_to_input]
                a.append(count)
                index_dic[place_to_input] = a
            puzzle_input.append(place_to_input)        
        count+=1


    print("ANS is:",puzzle_input[-1])


