def brain(tx):
	ext ="Sorry! Not able to understand properly, please try once again!" #general exception
	with open("brain.br") as mybrain:
		for line in mybrain:
			name, val = line.partition("=")[::2]
			if name == tx:
				txx = val
				return txx
	return ext
def ai(ttx):
	ext =ext ="Sorry! Not able to understand properly, please try once again!" #general exception
	with open("ai.br") as mybrain:
		for line in mybrain:
			name, val = line.partition("=")[::2]
			if name == ttx:
				txx = val
				return txx
	return ext
