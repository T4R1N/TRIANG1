from math import *

cardDirec = input("Is your direction 'N', 'S', 'E', or 'W'?\n> ")
if cardDirec == 'N' or cardDirec == 'S':
    cardDirec = 'North/South'
elif cardDirec == 'E' or cardDirec == 'W':
    cardDirec = 'East/West'
else:
    raise Exception("Input must be 'N', 'S', 'E', or 'W'.")

origX = float(input("Please input your original X value.\n> "))
origZ = float(input("Please input your original Z value.\n> "))

thetaOne = float(input("Please input the first angle value.\n> "))
meterTrav = float(input("Please input how many meters were traveled.\n> "))
thetaTwo = float(input("Please input the second angle value.\n> "))


match cardDirec:
    case 'North/South':
        destX = origX - (meterTrav / (tan(radians(90 - thetaOne))) - (tan(radians(90 - thetaTwo))))
        destZ = origZ + ((meterTrav * tan(radians(90-thetaOne)) / (tan(radians(90 - thetaOne)) - tan(radians(90 - thetaTwo)))))
    case 'East/West':
        destX = origX + (meterTrav * (tan(radians(thetaOne))) / ((tan(radians(thetaOne))) - (tan(radians(thetaTwo)))))
        destZ = origZ - (meterTrav / ((tan(radians(thetaOne))) - (tan(radians(thetaTwo)))))

print(f"The coordinates of the location you seek are ({destX}, {destZ}).")
