def prob_5(x0,x1,x2,y0,y1,y2):
	lis1=[]
	lis2=[]
	lis1.append(x0)
	lis1.append(x1)
	lis1.append(x2)
	lis2.append(y0)
	lis2.append(y1)
	lis2.append(y2)
	wx = (lis1[1]*lis2[2])-(lis1[2]*lis2[1])
	wy = (lis1[2]*lis2[0])-(lis1[0]*lis2[2])
	wz = (lis1[0]*lis2[1])-(lis1[1]*lis2[0])
	return [wx, wy,wz]