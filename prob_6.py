def prob_6(l):
	for n in range(len(l)-1,0,-1):
		for i in range(n):
			if l[i]>l[i+1]:
				t = l[i]
				l[i] = l[i+1]
				l[i+1] = t
return t