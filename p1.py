import numpy
import math 
add = 0
def check(val, checker):
	if(val<=checker):
		return 1
	else:
		return 0
for i in range(1,334,1):
	add = add+3*i+5*i*check(i,199)-15*i*check(i,66)
print(add)
