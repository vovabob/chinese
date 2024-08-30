#!/usr/bin/python -u 
# '-u' force stdout & stderr 'unbuffered'

import sys
import re

# You must supply a filename of the original text!
data = sys.argv[1]

with open(data, "r") as file:
	text = file.read().replace('\n','').replace(' ','').strip()

# Multiple patterns are enclosed in parens
# '3002' is 'Ideographic Full Stop'
# '3001' is 'Ideographic Comma'
# 'ff0c' is 'Fullwidth Comma'
# Unicode codepoints in Hex.
string = re.sub('([0-9]|\u3002|\u3001|\uff0c)', '', text )

# Make a set and "sort" it (by codepoints?!)
my_set = sorted( set(list(string)) )

for i in my_set :
	# use end=' ' if you need spaces between chars
	print(i, end='')

print()

# eof
