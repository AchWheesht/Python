"""This program calculates the volume of a sphere according to the biblical value of pi"""

#The formula to calculate the volume of a sphere is:
#Volume = (4 * pi * (r**3)) / 3

biblical_pi = 3
radius = int(input("Please enter the sphere's radius:\n"))
volume = (4 * biblical_pi * (radius**3)) / 3
print ("The volume of the sphere, as according to the most holy lord on high, is %s units cubed." % (volume))
