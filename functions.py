import turtle

def beam1():
    turtle.penup()
    turtle.goto(-400, 180)
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.left(30)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.end_fill()
    turtle.right(150)
    turtle.goto(400,180)
    turtle.begin_fill()
    turtle.left(30)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.end_fill()
    turtle.right(150)

def beam2(supp, length):
    turtle.penup()
    turtle.goto(-400, 180)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.left(30)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.end_fill()
    turtle.right(150)
    turtle.goto((supp/length*800)-400,180)
    turtle.begin_fill()
    turtle.left(30)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.end_fill()
    turtle.right(150)

def beam3():
    turtle.penup()
    turtle.goto(-400, 180)
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
    turtle.fillcolor("gray")
    turtle.begin_fill()
    turtle.forward(75)
    turtle.backward(175)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
    turtle.setheading(270)
    
def load1(mag, pos1, length, max_load):
    turtle.pu()
    turtle.goto((pos1/length*800)-400, 205)
    turtle.backward(mag/max_load*100)
    turtle.pd()
    turtle.write("{:.2f} kN".format(mag))
    turtle.forward(mag/max_load*100)
    turtle.stamp()
    
def load2(mag_start, start, mag_end, end, length, max_load):
    turtle.pu()
    turtle.goto((start/length*800)-400, 205)
    turtle.pd()
    turtle.stamp()
    turtle.backward(mag_start)
    turtle.write("{:.2f} kN/m".format(mag_start))
    turtle.goto((end/length*800)-400, 205 + mag_end/max_load*100)
    turtle.write("{:.2f} kN/m".format(mag_end))
    turtle.forward(mag_end/max_load*100)
    turtle.stamp()

def load3(mag, pos3, drc, length):
    turtle.pu()
    if drc == 1:
        turtle.goto((pos3/length*800)-400, 192.5)
        turtle.write("{:.2f} kNm".format(mag))
        turtle.goto((pos3/length*800)-400, 232.5)
        turtle.setheading(0)
        turtle.pd()
        turtle.circle(-40, 180)
        turtle.stamp()
        turtle.setheading(270)
    if drc == 2:
        turtle.goto((pos3/length*800)-400, 192.5)
        turtle.write(mag)
        turtle.write("{:.2f} kNm".format(mag))
        turtle.goto((pos3/length*800)-400, 152.5)
        turtle.setheading(0)
        turtle.pd()
        turtle.circle(40, 180)
        turtle.stamp()
        turtle.setheading(270)

def pos_r(mag_start, start, mag_end, end):
    loc1 = start + abs(start-end)/2
    if mag_start >= mag_end:
        loc2 = start + abs(start-end)/3
        F1 = mag_end * abs(start-end)
    if mag_end > mag_start:
        loc2 = start + abs(start-end)*2/3
        F1 = mag_start * abs(start-end)
    F2 = 0.5 * abs(start - end) * abs(mag_start - mag_end)
    Fr = 0.5 * abs(start - end) * (mag_start + mag_end)
    loc_r = (F1*loc1 + F2*loc2)/Fr
    return loc_r

def axes():
    turtle.pu()
    turtle.goto(-400, 80)
    turtle.setheading(90)
    turtle.stamp()
    turtle.write("Shear Force (kN)")
    turtle.setheading(270)
    turtle.pd()
    turtle.forward(175)
    turtle.backward(175/2)
    turtle.left(90)
    turtle.goto(400, -7.5)
    turtle.stamp()
    turtle.write("Distance (m)")
    turtle.right(90)
    turtle.pu()
    turtle.goto(-400,-120)
    turtle.setheading(90)
    turtle.stamp()
    turtle.write("Bending Moment (kNm)")
    turtle.setheading(270)
    turtle.pd()
    turtle.forward(175)
    turtle.backward(175/2)
    turtle.left(90)
    turtle.goto(400, -207.5)
    turtle.stamp()
    turtle.write("Distance (m)")
    turtle.pu()

def write_react(react1, react2=0, supp_pos = 400):
    turtle.pu()
    turtle.goto(-400, 130)
    turtle.pd()
    turtle.write("{:.2f} kN".format(react1))
    turtle.pu()
    turtle.goto(supp_pos,130)
    turtle.pd()
    turtle.write("{:.2f} kN".format(react2))

def find_extreme(force, drop, extreme):
    for i in range (1, len(drop)-1):
        force -= drop[i][1]
        extreme.append(force)

    if abs(max(extreme)) >= abs(min(extreme)):
        cornerstone = abs(max(extreme))

    if abs(min(extreme)) > abs(max(extreme)):
        cornerstone = abs(min(extreme))
    
    return cornerstone

def flat_graph(y):
    turtle.goto(-400, y)
    turtle.write("{:.2f}".format(0))
    turtle.pd()
    turtle.goto(400, y)
    turtle.pu()

def SFD(react, cornerstone, drop, length):
    turtle.goto(-400, react*75/cornerstone-7.5)
    turtle.write("{:.2f}".format(react))
    turtle.pd()
    turtle.goto(drop[1][0]*800/length-400, react*75/cornerstone-7.5)
    force = react
    turtle.write("{:.2f}".format(force))
    for points in range (1, len(drop)-1):
        if drop[points][2] == 1:
            force -= drop[points][1]
            turtle.goto(drop[points][0]*800/length-400, force*75/cornerstone-7.5)
            turtle.goto(drop[points+1][0]*800/length-400, force*75/cornerstone-7.5)
            turtle.write("{:.2f}".format(force))

        if drop[points][2] == 2:
            force -= drop[points][1]
            turtle.goto(drop[points][0]*800/length-400, force*75/cornerstone-7.5)
            if drop[points+1][2] != 2:
                turtle.goto(drop[points+1][0]*800/length-400, force*75/cornerstone-7.5)
                turtle.write("{:.2f}".format(force))
    turtle.goto(400, force*75/cornerstone-7.5)
    turtle.write("{:.2f}".format(force))
    turtle.pu()

def SFD2(react, cornerstone, drop, length):
    turtle.goto(-400, react*75/cornerstone-7.5)
    turtle.write("{:.2f}".format(react))
    turtle.pd()
    turtle.goto(drop[1][0]*800/length-400, react*75/cornerstone-7.5)
    force = react
    turtle.write("{:.2f}".format(force))
    for points in range (1, len(drop)-1):
        if drop[points][2] == 1 or drop[points][2] == 0:
            force -= drop[points][1]
            turtle.goto(drop[points][0]*800/length-400, force*75/cornerstone-7.5)
            turtle.goto(drop[points+1][0]*800/length-400, force*75/cornerstone-7.5)
            turtle.write("{:.2f}".format(force))

        if drop[points][2] == 2:
            force -= drop[points][1]
            turtle.goto(drop[points][0]*800/length-400, force*75/cornerstone-7.5)
            if drop[points+1][2] != 2:
                turtle.goto(drop[points+1][0]*800/length-400, force*75/cornerstone-7.5)
                turtle.write("{:.2f}".format(force))
    turtle.goto(400, force*75/cornerstone-7.5)
    turtle.write("{:.2f}".format(force))
    turtle.pu()

def BMD(bend_mom, cornerstone, length):
    turtle.goto(-400, -207.5)
    turtle.pd()
    for point in range (len(bend_mom)):
        turtle.goto(bend_mom[point][0]*800/length-400, bend_mom[point][1]*75/cornerstone-207.5)
        if abs(bend_mom[point][1]) == cornerstone:
            turtle.write("{:.2f}".format(bend_mom[point][1]))

def line_eq(mag_start, start, mag_end, end):
    y = [(mag_end-mag_start)/(end-start), mag_start]
    return y