def prob_11(pal):
	palabra = pal.split()
	s = "".join(palabra)
	var = s[::-1]
	if s == var:
		return ("es palindromo")
	else:
		return ("no es palindromo")