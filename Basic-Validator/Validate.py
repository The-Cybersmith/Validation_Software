#run this program with "python Validate.py -f Example-Geometry.txt"

import sys # used to allow command line things
import numpy # used to allow mathematical functions (like trigonometry) needed command: pip3 install numpy

#global variables below this line

filename = ""#this is stored globally because exceptions to its content my arise in various functions, and it could be useful for error messages

#global variables above this line

def Triangle_Check(A,B,C,X,Y,Z): #for non-right-angle triangles
    try:
        print("Checking angle sum.")
        if (180-(X+Y+Z) > 5): #some leeway to account for rounding errors
           return False
        return false
        #height is 2*Area/(base width)
        #expand this to derive whether this is valid (later)
    except ZeroDivisionError as e:
        print("Something about the contents of file \"" + filename + "\" has triggered a division by zero. This is almost certainly due to an error in the data.")
        return False

def Right_Angle_Triangle_Check(A,B,C,X,Y,Z): #assume angles are in degrees (that's what david said)
    try:
        print("Checking angle sum.")
        if (180-(X+Y+Z) > 5): #some leeway to account for rounding errors
           return False
        print("Checking Y validity.")
        if (Y > 92 or Y < 88): #some leeway, but Y should be a right angle
            return False
        print("Checking SOH.")
        if (numpy.absolute(numpy.sin(Z)/(A/C)) > 1.1 or numpy.absolute(numpy.sin(Z)/(A/C)) < 0.9): #SOH
            return False
        print("Checking CAH.")
        if (numpy.absolute(numpy.cos(Z)/(B/C)) > 1.1 or numpy.absolute(numpy.cos(Z)/(B/C)) < 0.9): #CAH
            return False
        print("Checking TOA.")
        if (numpy.absolute(numpy.tan(Z)/(A/B)) > 1.2 or numpy.absolute(numpy.tan(Z)/(A/B)) < 0.8): #TOA (larger margin for error needed)
            return False
        print("Checking Pythagoras.")
        if ((A*A)+(B*B) != (C*C)): #Pythagoras
            return False
        return True
    except ZeroDivisionError as e:
        print("Something about the contents of file \"" + filename + "\" has triggered a division by zero. This is almost certainly due to an error in the data.")
        return False

#Main execution begins here

print("---------Validation Program Beginning.")

if len(sys.argv) == 1:
    print("No additional arguments recieved.")
else:
    print("Additional arguments recieved: " + str(len(sys.argv) - 1))


print("This is the pattern your data must adhere to.")
print("A valid right-angled triangle is the only acceptable input.")
print("ABC are lengths and XYZ are angles.\n")


print("  X")
print("  |\\")
print("  | \\")
print("A |  \\ C")
print("  |   \\")
print("  |    \\")
print("Y ------ Z")
print("    B")

if '-f' in sys.argv:
    try:
        filename = sys.argv[sys.argv.index('-f') + 1]
    except IndexError as e:
        print("Warning! No filename in command line.")
        filename = input("Input file required for validation, please enter one here: ")
else:
    filename = input("Input file required for validation, please enter one here: ")

try:
    f = open(filename, 'r')
    print("Now reading from file.")
    A = float(f.readline())
    B = float(f.readline())
    C = float(f.readline())
    X = float(f.readline())
    Y = float(f.readline())
    Z = float(f.readline())
    print("Finished reading from file.")
    f.close
except FileNotFoundError as e:
    print("Warning! " + filename + " is a Non-valid file!")
    print("---------Validation Program Ending.")
    sys.exit(0)


if (Right_Angle_Triangle_Check(A,B,C,X,Y,Z)):
    print("The file \"" + filename + "\" contains viable data.")
else:
    print("The file \"" + filename + "\" contains NON-viable data.")

print("---------Validation Program Ending.")

#Main execution begins here
