the_count=[1,2,3,4,5]
fruits=['apples','oranges','watermelons','cherries']
change=[1, 'pennis', 2, 'dimes', 3, 'quarters']

#for-loop through a list
for number in the_count:
    print "This is count %d" %number

#same above
for fruit in fruits:
    print "A fruit of types: %s"%fruit

#also we can go through mixed lists as Well
#Since we don't know what's in it, we have to use %r
for cha in change:
    print "I got %r" %cha

#we can also build empty lists
elements=[]

for i in range(1,5):
    print "Adding %d to the list 'elements'"%i
    elements.append(i)

for i in elements:
    print "Element was %d" %i
