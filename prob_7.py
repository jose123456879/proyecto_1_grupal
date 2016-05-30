def prob_7 ():
	cuatro = []
	siete = []
	for i in range(0,250):
		cu = 4*i
		if cu < 1000:
			cuatro.append(cu)
		si = 7*i
		if si < 1000:
			siete.append(si)
	return (cuatro,siete)
