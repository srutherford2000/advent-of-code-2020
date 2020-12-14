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
waypoint_x = 10
waypoint_y = 1

for line in lines:
    direction = line[0]
    num = int(float(line[1:]))
    if direction == "N":
        waypoint_y += num
    elif direction == "S":
        waypoint_y -= num
    elif direction == "E":
        waypoint_x += num
    elif direction == "W":
        waypoint_x -= num
    elif direction == "R":
        rotations = num // 90      
        for i in range(rotations):
            temp = -1* waypoint_x
            waypoint_x = waypoint_y 
            waypoint_y = temp 
    elif direction == "L":
        rotations = num // 90      
        for i in range(rotations):
            temp = -1* waypoint_y
            waypoint_y = waypoint_x
            waypoint_x = temp 
    elif direction == "F":
        x += num * waypoint_x  
        y += num * waypoint_y 


ans = abs(x) + abs(y)

print("ANS is:",ans)
