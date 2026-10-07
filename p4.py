count = 0
def threedigit():
	maxm=0
	for i in range(999,99,-1):
		for j in range(999,99,-1):
			num = str(i*j)
			revnum = num[len(num)-1:len(num)//2-1:-1]
			numcopy = num[0:len(num)//2]
			if(numcopy==revnum):
				if(int(num)>maxm):
					maxm=int(num)
	return maxm				


if __name__=='__main__':
	print(threedigit())
