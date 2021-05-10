#WhAt IS YOUR NuMbER MuLTiPlIeD By ZeRO?!
def zeroMultiple(num):
	try:
		return ((int(num))*0)
	except:
		return ('An Error Has Occurred...\nPerhaps try not to input things that are not numbers (integers/real)')

print(zeroMultiple(input('Enter A Number To Multiply By Zero: ')))