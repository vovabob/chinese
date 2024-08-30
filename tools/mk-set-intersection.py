#!/usr/bin/python -u 

import sys
import re

# Both files MUST contain a 'set' of chars!
file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as f1 :
	s1 = set( f1.read().strip() )

with open(file2, "r") as f2 :
	s2 = set( f2.read().strip() )

common_chars = sorted( list( set.intersection(s1, s2) ) )

for c in common_chars :
	# use end=' ' if you need spaces between chars
	print(c, end='')

print()




