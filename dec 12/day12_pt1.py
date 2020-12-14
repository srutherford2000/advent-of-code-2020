import math

file_name=input('enter a file name')

in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()

angle = 0 # east
x = 0
y = 0 

for line in lines:
    direction = line[0]
    num = int(float(line[1:]))
    if direction == "N":
        y += num
    elif direction == "S":
        y -= num
    elif direction == "E":
        x += num
    elif direction == "W":
        x -= num
    elif direction == "R":
        angle -= num
    elif direction == "L":
        angle += num
    elif direction == "F":
        x += num * math.cos(math.radians(angle))
        y += num * math.sin(math.radians(angle))

ans = abs(x) + abs(y)

print("ANS is:",ans)
