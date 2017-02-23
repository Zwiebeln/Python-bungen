tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\r
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


'''
\t stands for tabbed in
\n stands for split a line
\\ stands for \
\' stands for '
\r Carriage Return
the presentation of octal and hex value is similar to that in JS
'''

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" %i,


#How to stop it? exit() doesn't work here
