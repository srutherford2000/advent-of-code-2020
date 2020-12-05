#file_name=input('enter a file name')
file_name = "input.txt"
in_file=open(file_name)
lines=[]

for line in in_file:
    lines.append(line.strip())

in_file.close()


def getSeatID(letters):
    frontBack = letters[:7]
    leftRight = letters[7:]
    range_fb = [0,127]
    range_lr = [0,7]
    for let in frontBack:
        current_set = range_fb[1] - range_fb[0]
        current_set //=2
        new_limit = current_set + range_fb[0]
        if let == "B":
            range_fb[0] = new_limit+1
        else:
            range_fb[1] = new_limit
    for let in leftRight:
        current_set = range_lr[1] - range_lr[0]
        current_set //=2
        new_limit = current_set + range_lr[0]
        if let == "R":
            range_lr[0] = new_limit+1
        else:
            range_lr[1] = new_limit

    return [range_fb[0],  range_lr[0]]

def calcSeatIDfromNum(orderPair):
    return orderPair[0]*8 + orderPair[1]

#read in the input file into a list of full seats
list_of_full_seats = []
for line in lines:
    Id = getSeatID(line)
    list_of_full_seats.append(Id)
list_of_full_seats.sort()

#find the open seats
list_of_open_seats = []
for i in range(1,127):
    for j in range(0,8):
        if [i,j] not in list_of_full_seats:
            list_of_open_seats.append([i,j])

#get a list of seat ids for full seats
list_of_curr_seat_ids = []
for seat in list_of_full_seats:
    x = calcSeatIDfromNum(seat)
    list_of_curr_seat_ids.append(x)

#go through empty seats and see if they have adjacent seat ids that are full
for seat in list_of_open_seats:
    y = calcSeatIDfromNum(seat)
    if (y+1 in list_of_curr_seat_ids) and (y-1 in list_of_curr_seat_ids):
        print("seat:",seat,"with id of:", y)
