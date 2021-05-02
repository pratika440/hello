import re
hand = open('sample.txt')
print( sum( [ re.findall for line in hand('[0-9]+','sample.txt'.read()) ] ) )