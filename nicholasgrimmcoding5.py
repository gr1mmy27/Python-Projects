'''Creating a program that works with projectile motion'''
import math

# March 8, 2023
# Nicholas Grimm
# CS-1300

# CREATIVE ELEMENT - I added in gravitational acceleration followed by 
# entering the angle from the starting point to calculate 

# constants
G = 9.81  # gravitational acceleration

# get user input
v0 = float(input("Enter the initial velocity (m/s): "))
theta = float(input("Enter the angle of launch (degrees): "))
h0 = float(input("Enter the initial height (m): "))

# calculate components of initial velocity
vx0 = v0 * math.cos(math.radians(theta))
vy0 = v0 * math.sin(math.radians(theta))

# calculate time of flight
t_flight = 2 * vy0 / G

# create arrays for time and height
dt = 0.1  # time step size
t = [i * dt for i in range(int(t_flight/dt)+1)]
h = [h0 + vy0*t[i] - 0.5*G*t[i]**2 for i in range(len(t))]

# print results
print(f"Time of flight: {t_flight:.2f} s")
print(f"Maximum height: {max(h):.2f} m")

# ask user for time input
while True:
    t_input = float(input("Enter a time during the flight (s): "))
    if t_input < 0 or t_input > t_flight:
        print("Invalid time. Please enter a time between 0 and {:.2f} s.".format(t_flight))
    else:
        break

# calculate and print height at input time
idx = int(t_input/dt)
print("Height at time {:.2f} s: {:.2f} m".format(t_input, h[idx]))