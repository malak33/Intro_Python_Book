#cball1.y
from math import sin, cos, radians

def main():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    hO = eval(input("enter the initial height (in meters) : "))
    time = eval(input("Enter the time interval between positions calculations: "))

    # convert angle to radians
    theta = radians(angle)

    # set the initla position and velocities in x and y directions
    xpos = 0
    ypos = hO
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    # loop until the ball hits the ground
    while ypos >= 0.0:
        #calculate posistion and velocity in time seconds
        xpos = ypos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

if __name__ == '__main__': main()
