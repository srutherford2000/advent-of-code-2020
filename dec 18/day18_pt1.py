def find_outer_parens(s):
    toret = {}
    pstack = []
    first_ind = len(s)

    for i, c in enumerate(s):
        if c == '(':
            if i < first_ind:
                first_ind = i
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    last_ind = toret[first_ind]
    
    return (first_ind,last_ind,s[first_ind+1:last_ind])
    


def solve(string):
        if "(" in string:
            x = find_outer_parens(string)
            first_ind = x[0]
            last_ind = x[1]
            new_string = x[2]
            sum_of_subsection = solve(new_string)
            string = string[:first_ind] + str(sum_of_subsection) + string[last_ind+1:]
            return solve(string)
        elif string.isnumeric():
            return int(string)
        else:
            try:
                plus_ind = string.index("+")
            except ValueError:
                plus_ind = len(string)
            try:
                star_ind = string.index("*")
            except ValueError:
                star_ind = len(string)
            if plus_ind < star_ind: #plus is the operand
                first_num = string[:plus_ind]
                operand = "+"
                try:
                    second_plus_ind = string[plus_ind + 1 :].index("+") + plus_ind + 1
                except ValueError:
                    second_plus_ind = len(string)
                if second_plus_ind < star_ind: #second operand is plus
                    second_num = string[plus_ind+1: second_plus_ind]
                    final_ind = second_plus_ind
                else: #second operand is star
                    second_num = string[plus_ind+1: star_ind]
                    final_ind = star_ind
            else: # star is first
                first_num = string[:star_ind]
                operand = "*"
                try:
                    second_star_ind = string[star_ind + 1 :].index("*") + star_ind + 1
                except ValueError:
                    second_star_ind = len(string)
                if second_star_ind < plus_ind: #second operand is star
                    second_num = string[star_ind+1: second_star_ind]
                    final_ind = second_star_ind
                else: #second operand is plus
                    second_num = string[star_ind+1: plus_ind]
                    final_ind = plus_ind
            if operand == "+":
                total = int(first_num)+int(second_num)
            else:
                total = int(first_num)* int(second_num)
            string = str(total) + string[final_ind:]
            return solve(string)


file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

running_sum = 0

for line in lines:
    line = line.replace(" ","")
    line_total = solve(line)
    running_sum += line_total

print("ANS is:", running_sum)



