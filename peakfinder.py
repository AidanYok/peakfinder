

def peakFinder(f, initVal, lastVal, delta):
	if (initVal % 2 == 1):
		print('Odd intitVal, must be even, adding 1')
		initVal = initVal + 1

	if (delta == 1):
		return initVal
	
	initResult = lastVal
	a = f(initVal - delta)
	b = f(initVal + delta)
	
	if (a > initResult and a > b):
		peakFinder(f,initVal - delta, a, delta)
	elif (b > initResult and b > a):
		peakFinder(f,initVal + delta, b, delta)
	elif (a and b < initResult):
		peakFinder(f, initVal, initResult, (delta / 2))
	else:
		print('error, this code is scuffed')
		return null
