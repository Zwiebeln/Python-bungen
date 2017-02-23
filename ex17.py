#Copy the content of a file to another file

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

in_file = open(from_file) # the default mode is read mode
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

#python doesn't promise that it will close the files, but operating system does. 
out_file.close()
in_file.close()

'''
You can use:
    echo "xxx"> filename.txt
to create a file

And use:
    cat filenam.txt
to open a file like before
'''
