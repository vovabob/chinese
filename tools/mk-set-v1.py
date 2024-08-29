#!/usr/bin/python -u 

import sys
import re

# You must supply a filename of the original text
data = sys.argv[1]

with open(data, "r") as file:
	text = file.read()

# Concat all lines into one lo-o-o-ong string.
string = re.sub( r'\n', '', text.strip() )

set1 = set(list(string))

for i in set1:
	# use end=' ' if you need spaces between chars
	print(i, end='')

print()

# eof
