import collections
import json
print("starting")

ciphertext = "llzvvqadpwieixgsgmjbosryarpafkjvjcddcdrtufleomfhkarolzmudenwrmkmgcmuiflistvwleeicfzqgyosrjhjixmrnwllzwlvldingzyfuivruypsgoeinlzeomjjglmjrducarblfqwnimjfllzsnijydwgojvqozsksjmwkwolvjjwhdwgikaxdsecusroirwzqsplfqlgfzaznuzxcidcfveihvhkfemikbwkiiwvmaueixvfdqsplfqlgfjxkfwxehislwokgsissfhzzvhhmxvwkihhimmexwsxcxyyfskvmegsqfzwfgwgjtslbsnixsdylgljknujlwdrgikkinwzifgjvfzfalmzwjixgvhmuutdiolrnqgyaivfugramuyfliislazlsiskjsqeoxvhlasi"

print(len("llzvvqadpwieixgsgmjbosryarpafkjvjcddcdrtufleomfhkarolzmudenwrmkmgcmuiflistvwleeicfzqgyosrjhjixmrnw"))
print(len("llzwlvldingzyfuivruypsgoeinlzeomjjglmjrducarblfqwnimjf"))


######################################################################
def get_factors(x):
   # This function takes a number and prints the factors
   res = []
   for i in range(1, x + 1):
       if x % i == 0:
           res.append(i)
   return res
######################################################################           

val = ciphertext.split("llz")
lengths = []

for x in val:
	if len(x)>0 and x != val[len(val)-1] :
		lengths.append(len(x) + 3)
print("lengths:", lengths)


factors = []
for y in lengths:
	factors.append(get_factors(y))

print("factors:", factors)

commonFactors = list(set(factors[0]).intersection(factors[1]))
print("commonFactors: ", commonFactors)

##########################################################################
n = 2
mapper = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]

n1 = []
n2 = []

for letter in mapper:
	try:		
		n1.append(letter[0])
	except IndexError:
		print("nothing")
	try:		
		n2.append(letter[1])
	except IndexError:
		print("nothing")


print (n1)
print (n2)

n1String = ''.join(n1)
n2String = ''.join(n2)

print (n1String)
print (n2String)

print(collections.Counter(n1String).most_common(1)[0])
print(collections.Counter(n2String).most_common(1)[0])

class cipherChar:
	def __init__(self, cipherString):
		self.cipherString = cipherString
		self.a = cipherString.count('a')
		self.b = cipherString.count('b')
		self.c = cipherString.count('c')
		self.d = cipherString.count('d')
		self.e = cipherString.count('e')
		self.f = cipherString.count('f')
		self.g = cipherString.count('g')
		self.h = cipherString.count('h')
		self.i = cipherString.count('i')
		self.j = cipherString.count('j')
		self.k = cipherString.count('k')
		self.l = cipherString.count('l')
		self.m = cipherString.count('m')
		self.n = cipherString.count('n')
		self.o = cipherString.count('o')
		self.p = cipherString.count('p')
		self.q = cipherString.count('q')
		self.r = cipherString.count('r')
		self.s = cipherString.count('s')
		self.t = cipherString.count('t')
		self.u = cipherString.count('u')
		self.v = cipherString.count('v')
		self.w = cipherString.count('w')
		self.x = cipherString.count('x')
		self.y = cipherString.count('y')
		self.z = cipherString.count('z')

cc1 = cipherChar(n1String)
attrs1 = vars(cc1)
cc2 = cipherChar(n2String)
attrs2 = vars(cc2)
# {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
# now dump this in some way or another
print ('\n'.join("%s: %s" % item for item in attrs1.items()))
print('\n\n\n')
print ('\n'.join("%s: %s" % item for item in attrs2.items()))

