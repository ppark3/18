f = open("MobyDick.txt", "r")
list = f.read().lower().split()
f.close()

def frequency(word, x):
	return len([i for i in x if i == word])
	
print frequency("happy", list)
print frequency("angry", list)
	
def frequencies(words, x):
	return reduce(lambda a, b: frequency(a, x) + frequency(b, x), words)
	
print frequencies(["happy","angry"], list)

def frequent(x):
	return reduce(lambda a, b: a if frequency(a, x) > frequency(b, x) else b, x)
	
print frequent(list)