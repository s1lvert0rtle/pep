import math

def series():
	i=1
	iprev=1
	add = 0
	while(i<4000000):
		c = str(i)
		if c[len(c)-1] in '02468':
			print(i)
			add = add+i
		k=i
		i=iprev+i
		iprev=k
	print(add)

if __name__=='__main__':
	series()

