my_name = "Zwiebel"
my_age = 5
my_height = 164
my_weight = 66
my_eyes = 'green'
my_teeth = 'sparse and yellow like the stars'
my_hair = 'green'

print "Let's talk about %s." %my_name
print "She's %d inches tall and %d pounds heavy" % (my_height, my_weight)
print "Actually that's not too heavy"
print "She got %s eyes and %s hair" % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee" % my_teeth

print "If I add %d, %d, and %d, I get %d" %(my_age, my_height, my_weight,my_age+my_height+my_weight)

#you can also replace '' with "" in the declaration
# %r stand for "print no matter what"
print "No matter %r" % "what"
print "No matter %r" % 'what'
my_string= 'what'
print "no matter %r" % my_string
print "no matter %s" % my_string
#format characters https://docs.python.org/3/library/stdtypes.html#str.format
