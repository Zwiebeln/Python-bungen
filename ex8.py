formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("Do not go gentle into that good night.", "Old age should burn" +
 "and rave at close of day.",
"Rage,", "rage against the dying of the light")
