def calculatorStandard(s):
    #// parse one or more level-1 expressions separated by +'s
    def calc2(i):
        (sumy,j) = calc1(i)
        while (s[j] == '*'):
            (x,k) = calc1(j+1)
            sumy *= x
            j = k
        return (sumy,j)

    def calc1(i):
    #// parse one or more level-0 expressions separated by *'s
        (mult,j) = calc0(i)
        while (s[j] == '+'):
            (x,k) = calc0(j+1)
            mult += x
            j = k
        return (mult,j)

    def calc0(i):
    #// parse a single digit, or a level-2 expression in parentheses
        if (s[i].isnumeric()):
            return (int(float(s[i])), i+1)
        else:
            (x,j) = calc2(i+1)
            return (x,j+1)
    x = calc2(0)
    return x[0]

file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

running_sum = 0

for line in lines:
    line = line.replace(" ","")
    line += "!"
    line_total = calculatorStandard(line)
    running_sum += line_total

print("ANS is:", running_sum)
