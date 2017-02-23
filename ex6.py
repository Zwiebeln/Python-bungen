# Both "" and '' stand for string
# format characters: %, ()
x = "There are %d types of people" %10
binary = "binary"
do_not = "don't"
#string inside a string, #string inside a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#string inside a string
print "I said: %r." %x

#string inside a string
print "I also said: '%s'" %y

#capitalized F!!!
hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# two variables are now connected by +
print w + e
