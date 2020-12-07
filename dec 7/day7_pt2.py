file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()


rule_dict = {}

for line in lines:
    x = line.split(" contain ")
    key = x[0]
    if "bags" in key:
        key = key[:-5]
    else:
        key = key[:-4]
        
    val = x[1]
    newbaglist = []
    x = val[:-1].split(", ")
    if (x[0] == "no other bags"):
        pass
    else:
        for bag in x:
            if "bags" in bag:
                newbaglist.append(bag[ : -5 ])
            else:
                newbaglist.append(bag[ : -4 ])
    rule_dict[key] = newbaglist



def findSum (aBag):
    if (rule_dict.get(aBag) == []):
        return 1
    else:
        val = rule_dict.get(aBag)
        theSum = 1
        for i in val:
            ind = i.index(" ")
            num = int(float(i[:ind]))
            word = i[ind+1:]
            theSum += num * findSum(word)
        return theSum

        
        
print(findSum("shiny gold")-1)
