def find_2020th_Term(input_string):
    puzzle_input = input_string.split(",")
    for i in range(len(puzzle_input)):
        num_as_str = puzzle_input[i]
        num = int(num_as_str)
        puzzle_input[i] = num

    count =len(puzzle_input)

    while count < 2020:
        current_ind = count - 1
        last_num = puzzle_input[current_ind]
        if (puzzle_input.count(last_num) <2):##means its the 1st occurance
            puzzle_input.append(0)
        else:
            previous_occurance_ind = len(puzzle_input) - (puzzle_input[:-1][::-1].index(last_num)+1) - 1
            place_to_input  = current_ind - previous_occurance_ind
            puzzle_input.append(place_to_input)        
        count+=1

    print("ANS is:",puzzle_input[-1])

