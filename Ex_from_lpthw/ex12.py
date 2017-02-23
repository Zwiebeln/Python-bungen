#Be careful with the space after the question mark
age = raw_input("How old are you? ")
height =raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you are %s old, %s tall and %s heavy" %(
age, height, weight)

'''
After typing pydoc raw_input:

raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.
(END)

Then type q to quite the doc
'''
