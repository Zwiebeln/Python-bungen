print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

#raw_input is really much easier than JOptionPane!!!!!!

#the standard one
print "So, you're %s old, %s tall and %s heavy" %(age, height, weight)

'''
The one with '' around each input
print "So, you're %r old, %r tall and %r heavy" %(age, height, weight)

Even if all input are given in numbers, this line doesn't work. Because
just like in Java, the input numbers are also strings.
But you can cast them by x= int(raw_input())
print "So, you're %d old, %d tall and %d heavy" %(age, height, weight)
'''
