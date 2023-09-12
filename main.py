# import libraries
import functions
import turtle
from operator import itemgetter

# default values
x0 = -400
y01 = -7.5
y02 = -207.5

# list initializations
load_list = []
mags = [0]
moment_list = []
force_list = []
drop = []
BM_drop = []
bend_mom = []
extreme_1 = []
extreme_2 = []
inputs =[]

# user inputs
# manual or through file?
print("Origin of data:")
print("1. Manual input (for new data)")
print("2. File (for previously entered data)") 

valid = True
while valid:
    try:
        origin = int(input("Select from [1] or [2]: "))
        while origin not in [1, 2]:
            origin = int(input("Select from [1] or [2]: "))
        valid = False
    except ValueError:
        continue

if origin == 1:
    # beam selection
    print("Types of statically determinate beams:")
    print("1. Simply Supported Beam")
    print("2. Over-hanging Beam")
    print("3. Cantilever Beam")

    valid = True
    while valid:
        try:
            types = int(input("Select beam from type [1], [2], or [3]: "))
            while types not in [1, 2, 3]:
                types = int(input("Select beam from type [1], [2], or [3]: "))
            valid = False
        except ValueError:
            continue

    inputs.append(types)

    if types == 1:
        valid = True
        while valid:
            try:
                length = float(input("Enter the length of the beam: "))
                valid = False
            except ValueError:
                continue
        inputs.append(length)
    
    if types == 2:
        valid = True
        while valid:
            try:
                length = float(input("Enter the length of the beam: "))
                supp = float(input("Position of the movable support from left end of the beam:"))
                while supp > length or supp == 0:
                    supp = float(input("Position of the movable support from left end of the beam:"))
                valid = False
            except ValueError:
                continue
        inputs.append(length)
        inputs.append(supp)
             
    if types == 3:
        valid = True
        while valid:
            try:
                length = float(input("Enter the length of the beam: "))
                valid = False
            except ValueError:
                continue
            inputs.append(length)

    # load selection
    print("Types of loads:")
    print("1. Concentrated Load")
    print("2. Distributed Load")
    print("3. Bending Moment")

    # storing loads in a list
    load_list.append((0,0,0))
    while True:
        load = input("Select load from type [1], [2], or [3] (0 if no more loads to be added): ")
        while load not in "0123":
            load = input("Select load from type [1], [2], or [3] (0 if no more loads to be added): ")
        if load == "1":
            valid = True
            while valid:
                try:
                    mag = float(input("Enter the magnitude of force: "))
                    pos1 = float(input("Enter the position of the force from the left end of the beam: "))
                    valid = False
                    while pos1 > length or pos1 < 0:
                        pos1 = float(input("Enter the position of the force from the left end of the beam: "))
                    load_list.append((1, mag, pos1))
                    mags.append(mag)
                except ValueError:
                    continue

        if load == "2":
            valid = True
            while valid:
                try:
                    mag_start = float(input("Enter the magnitude of force at the beginning of the distribution: "))
                    start = float(input("Enter the position of the force from the left end of the beam: "))
                    mag_end = float(input("Enter the magnitude of force at the end of the distribution: "))
                    end = float(input("Enter the position of the force from the left end of the beam: "))
                    valid = False
                    while start > length or start < 0:
                        start = float(input("Enter the position of the force from the left end of the beam: "))
                    while end > length or end <= start or end < 0:
                        end = float(input("Enter the position of the force from the left end of the beam: "))
                    load_list.append((2, mag_start, start, mag_end, end))
                    mags.append(mag_start)
                    mags.append(mag_end)
                except ValueError:
                    continue

        if load == "3":
            valid = True
            while valid:
                try:
                    mag = float(input("Enter the magnitude of the moment: "))
                    pos3 = float(input("Enter the position of the moment from the wall: "))
                    valid = False
                    while pos3 > length or pos3 < 0:
                        pos3 = float(input("Enter the position of the moment from the wall: "))
                    drc = int(input("[1] Clockwise or [2] Anti-clockwise: "))
                    while drc not in [1, 2]:
                        drc = int(input("[1] Clockwise or [2] Anti-clockwise: "))
                    load_list.append((3, mag, pos3, drc))
                except ValueError:
                    continue
        if load == "0":
            break
    for i in range (1, len(load_list)):
        for j in range (len(load_list[i])):
            inputs.append(load_list[i][j])
    inputs.append(0)

    load_list.append((0,0,length))

    # writing the data file
    current = open("current.txt", "w")
    for i in range (len(inputs)):
        print(inputs[i], file = current)
    current.close()

if origin == 2:
    current = open("current.txt", "r")
    for line in current:
        line = line.replace("\n", "")
        inputs.append(line)
        
    load_list.append((0,0,0))
    # reading the data file
    i = 0
    if inputs[0] == "1":
            types = int(inputs[i])
            length = float(inputs[i+1])
            i += 2
    if inputs[0] == "2":
        types = int(inputs[i])
        length = float(inputs[i+1])
        supp = float(inputs[i+2])
        i += 3
    if inputs[0] == "3":
        types = int(inputs[i])
        length = float(inputs[i+1])
        i += 2

    for item in range (i, len(inputs)):
        if inputs[i] == "1":
            load = int(inputs[i])
            mag = float(inputs[i+1])
            pos = float(inputs[i+2])
            load_list.append((load, mag, pos))
            mags.append(mag)
            i += 3
        if inputs[i] == "2":
            load = int(inputs [i])
            mag_start = float(inputs[i+1])
            start = float(inputs[i+2])
            mag_end = float(inputs[i+3])
            end = float(inputs[i+4])
            load_list.append((load, mag_start, start, mag_end, end))
            mags.append(mag_start)
            mags.append(mag_end)
            i += 5
        if inputs[i] == "3":
            load = int(inputs [i])
            mag = float(inputs[i+1])
            pos = float(inputs[i+2])
            drc = float(inputs[i+3])
            load_list.append((load, mag, pos, drc))
            i += 4
        if inputs[i] == "0":
            break
    load_list.append((0,0,length))
    current.close()

screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
turtle.speed(0)

# drawing the beam
if types == 1:
    functions.beam1()

if types == 2:
    functions.beam2(supp, length)

if types == 3:
    functions.beam3()

max_load = max(mags)

# drawing the loads
for loads in load_list:
    if loads[0] == 1:
        functions.load1(loads[1], loads[2], length, max_load)
        moment_list.append(loads[1]*loads[2])
        force_list.append(loads[1])
    if loads[0] == 2:
        functions.load2(loads[1], loads[2], loads[3], loads[4], length, max_load)
        moment_list.append(0.5 * abs(loads[2] - loads[4]) * (loads[1] + loads[3])*functions.pos_r(loads[1], loads[2], loads[3], loads[4]))
        force_list.append(0.5 * abs(loads[2] - loads[4]) * (loads[1] + loads[3]))
    if loads[0] == 3:
        functions.load3(loads[1], loads[2], loads[3], length)
        if loads[3] == 1:
            moment_list.append(loads[1])
        if loads[3] == 2:
            moment_list.append(-loads[1])

# calculating reaction forces
if types == 1:
    react2 = sum(moment_list)/length
    react1 = sum(force_list) - react2
    functions.write_react(react1, react2)
    drop.append((0, react1, 0))
if types == 2:
    react2 = sum(moment_list)/supp
    react1 = sum(force_list) - react2
    load_list.append((4, react2, supp))
    functions.write_react(react1, react2, (supp/length*800)+x0)
    drop.append((0, react1, 0))
    drop.append((supp, -react2, 0))
    drop.append((length, 0, 0))
if types == 3:
    react = sum(force_list)
    moment = sum(moment_list)
    turtle.pu()
    turtle.goto(-400, 180)
    turtle.write("{:.2f} kN".format(react))
    drop.append((0, react, 0))

# drawing the beam axes
functions.axes()

load_list = sorted(load_list, key = itemgetter(2))

# drawing the graphs
if types == 1:
    force = react1
    extreme_1.append(react1)
    for loads in load_list:
        if loads[0] == 0:
            continue
        if loads[0] == 1:
            if loads[2] == length:
                drop.append((loads[2], 0, 1))
                continue
            drop.append((loads[2], loads[1], 1))
            force -= loads[1]

        if loads[0] == 2:
            for x in range (101):
                y = functions.line_eq(loads[1], loads[2], loads[3], loads[4])
                drop.append(((loads[2]+x*abs(loads[2]-loads[4])/100), (y[0]*(x*abs(loads[4]-loads[2])/100)+y[1])*(abs(loads[4]-loads[2])/100), 2))
                force -= y[0]*(x*abs(loads[4]-loads[2])/100)+y[1]*abs(loads[4]-loads[2])/100
            
        if loads[0] == 3:
            if loads[3] == 1:
                BM_drop.append((loads[2], -loads[1], 3))
            if loads[3] == 2:
                BM_drop.append((loads[2], loads[1], 3))

    drop = sorted(drop, key = itemgetter(0))
    drop.append((length, -react2, 0))

    cornerstone = functions.find_extreme(react1, drop, extreme_1)
    
    if cornerstone == 0:
        functions.flat_graph(y01)

    else:
        functions.SFD(react1, cornerstone, drop, length)

    drop = drop + BM_drop + [(length, 0 ,0)]
    drop = sorted(drop, key = itemgetter(0))

    force = react1
    moment = 0

    for i in range (1, len(drop)-1):
        if drop[i][2] == 1 or drop[i][2] == 2 or drop[i][2] == 0:
            moment += force*(drop[i][0]-drop[i-1][0])
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))
            force -= drop[i][1]
        if drop[i][2] == 3:
            moment += force*(drop[i][0]-drop[i-1][0])
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))
            moment += -drop[i][1]
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))

    if abs(max(extreme_2)) >= abs(min(extreme_2)):
        cornerstone = abs(max(extreme_2))

    if abs(min(extreme_2)) > abs(max(extreme_2)):
        cornerstone = abs(min(extreme_2))

    if cornerstone == 0:
        functions.flat_graph(y02)
    else: 
        functions.BMD(bend_mom, cornerstone, length)   

if types == 2:
    force = react1
    extreme_1.append(react1)
    for loads in load_list:
        if loads[0] == 1:
            if loads[2] == supp:
                drop.remove((supp, -react2, 0))
                drop.append((supp, loads[1]-react2, 1))
            else:
                drop.append((loads[2], loads[1], 1))

        if loads[0] == 2:
            for x in range (101):
                y = functions.line_eq(loads[1], loads[2], loads[3], loads[4])
                drop.append(((loads[2]+x*abs(loads[2]-loads[4])/100), (y[0]*(x*abs(loads[4]-loads[2])/100)+y[1])*(abs(loads[4]-loads[2])/100), 2))
                force -= y[0]*(x*abs(loads[4]-loads[2])/100)+y[1]*abs(loads[4]-loads[2])/100

        if loads[0] == 3:
            if loads[3] == 1:
                BM_drop.append((loads[2], -loads[1], 3))
            if loads[3] == 2:
                BM_drop.append((loads[2], loads[1], 3))
                
    drop = sorted(drop, key = itemgetter(0))

    cornerstone = functions.find_extreme(react1, drop, extreme_1)
    
    if cornerstone == 0:
        functions.flat_graph(y01)
    else:
        functions.SFD2(react1, cornerstone, drop, length)
    
    drop = drop + BM_drop + [(length, 0 ,0)]
    drop = sorted(drop, key = itemgetter(0))

    force = react1
    moment = 0

    for i in range (1, len(drop)-1):
        if drop[i][2] == 1 or drop[i][2] == 2 or drop[i][2] == 0:
            moment += force*(drop[i][0]-drop[i-1][0])
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))
            force -= drop[i][1]
        if drop[i][2] == 3:
            moment += force*(drop[i][0]-drop[i-1][0])
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))
            moment += -drop[i][1]
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))

    if abs(max(extreme_2)) >= abs(min(extreme_2)):
        cornerstone = abs(max(extreme_2))

    if abs(min(extreme_2)) > abs(max(extreme_2)):
        cornerstone = abs(min(extreme_2))

    if cornerstone == 0:
        functions.flat_graph(y02)
    else: 
        functions.BMD(bend_mom, cornerstone, length)

if types == 3:
    force = react
    extreme_1.append(react)
    for loads in load_list:
        if loads[0] == 1:
            drop.append((loads[2], loads[1], 1))

        if loads[0] == 2:
            for x in range (101):
                y = functions.line_eq(loads[1], loads[2], loads[3], loads[4])
                drop.append(((loads[2]+x*abs(loads[2]-loads[4])/100), (y[0]*(x*abs(loads[4]-loads[2])/100)+y[1])*(abs(loads[4]-loads[2])/100), 2))
                force -= y[0]*(x*abs(loads[4]-loads[2])/100)+y[1]*abs(loads[4]-loads[2])/100
            
        if loads[0] == 3:
            if loads[3] == 1:
                BM_drop.append((loads[2], -loads[1], 3))
            if loads[3] == 2:
                BM_drop.append((loads[2], loads[1], 3))

    drop = sorted(drop, key = itemgetter(0))
    drop.append((length, 0, 0))

    cornerstone = functions.find_extreme(react, drop, extreme_1)

    if cornerstone == 0:
        functions.flat_graph(y01)
    else:
        functions.SFD(react, cornerstone, drop, length)

    drop = drop + BM_drop + [(length, 0 ,0)]
    drop = sorted(drop, key = itemgetter(0))

    force = react
    moment = -moment
    extreme_2.append(moment)

    for i in range (1, len(drop)-1):
        if drop[i][2] == 1 or drop[i][2] == 2 or drop[i][2] == 0:
            moment += force*(drop[i][0]-drop[i-1][0])
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))
            force -= drop[i][1]
        if drop[i][2] == 3:
            moment += force*(drop[i][0]-drop[i-1][0])
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))
            moment += -drop[i][1]
            extreme_2.append(moment)
            bend_mom.append((drop[i][0], moment))

    if abs(max(extreme_2)) >= abs(min(extreme_2)):
        cornerstone = abs(max(extreme_2))

    if abs(min(extreme_2)) > abs(max(extreme_2)):
        cornerstone = abs(min(extreme_2))

    if cornerstone == 0:
        functions.flat_graph(y02)
    else: 
        functions.BMD(bend_mom, cornerstone, length)
            
turtle.hideturtle()
turtle.done()
