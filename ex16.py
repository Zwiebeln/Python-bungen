from sys import argv

script, filename= argv

print "We are going to erase %r" % filename
print "If you don't want that, hit Control+C (^C)."
print "If you do want that, hit RETRUN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')  #write mode
'''
'w': open this file in write mode
'r': read
'a': append and modify
'''


#Imagine use truncate() for a databank..
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print "And finally, we close it."
target.close()
