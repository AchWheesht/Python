"""This program calculates the area of a trapezoid"""

#The formula for the area of a trapezoid is:
#0.5 * ((a + b)*c)
#Where:
#a is the length of the bottom base
#b is length of the top base
#c is the height of the trapezoid

bottom_base_length = int(input("Please enter the length of the bottom base\n"))
top_base_length = int(input("Please enter the length of the top base\n"))
trapezoid_height = int(input("Please enter the heigh of the trapezoid\n"))

trapezoid_area = ((bottom_base_length + top_base_length) * trapezoid_height) * 0.5

print("The area of the trapezoid is %s units squared" % (trapezoid_area))
