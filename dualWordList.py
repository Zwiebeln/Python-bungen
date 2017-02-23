#author: Zwiebel
# -*- coding: utf-8 -*-import collections
from collections import Counter

#default value mode is read mode
from_file = open("happiness_seg.txt")

content = from_file.read().decode('utf8')
seglist = content.split()

#returns a list with most frequent used dual words
def count_most_frequent(a):
    dual_words = []
    for i in range(0, len(a)-1):
        if(len(a[i])>=2 and len(a[i+1])>=2):
            dual_words.append(a[i]+ " " + a[i+1])
    return Counter(dual_words).most_common(10)

#print out the results from list
def print_out(input_list):
    for word in input_list:
        print  " %s: %d" %(word[0], word[1])

print_out(count_most_frequent(seglist))
