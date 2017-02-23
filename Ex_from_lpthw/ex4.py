# no semicolon after each declaration!
cars= 100
#not "camel"?
space_in_a_car =4
drivers =30
passengers =90
cars_not_driven = cars- drivers
cars_driven = drivers
carpool_capacity = cars_driven* space_in_a_car
average_passengers_per_car = passengers/ cars_driven

# Spaces are saved automatically between each part of a line!!!
print "There are ", cars, "cars available."
print "There are only", drivers, " drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
#no auto correction for other languages?
print "Wir haben", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "explaination for traceback in the tutorial: use the wrong name of variable"
print "4.0 is not necessary. Because it's hard to get half car", "tested"

print "If you want to print without spaces, try '%'"
print "Hey %s there." % "you"
#You can use %s to stand for a variable
