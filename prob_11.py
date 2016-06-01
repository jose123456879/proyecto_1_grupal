def prob_11(pal):
	palabra = pal.split()
	pal.split()
	j = "".join(palabra)
	d = palabra.reverse()
	pal2=pal.split()
	s = "".join(pal2)
	if d == s:
		return ("es palindromo")
	else:
		return ("no es palindromo")