from sys import argv

script, first, second, third = argv

name = raw_input("The last input is: ")

print "The script is called:", script #This can be captured automatically
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "The last input is", name

#Use another way to run it:
#python ex13.py frist 2nd 3rd, to input arguments into argv

'''
If you give only two arguments:
ValueError: need more than 2 values to unpack

If you give more than 3 arguments:
ValueError: too many values to unpack

Each input argument are separated with space
e.g:
python ex13.py aa, bb,cc, dd
Your second variable is: bb,cc
'''
