import collections
import json
print("starting")

ciphertext = "llzvvqadpwieixgsgmjbosryarpafkjvjcddcdrtufleomfhkarolzmudenwrmkmgcmuiflistvwleeicfzqgyosrjhjixmrnwllzwlvldingzyfuivruypsgoeinlzeomjjglmjrducarblfqwnimjfllzsnijydwgojvqozsksjmwkwolvjjwhdwgikaxdsecusroirwzqsplfqlgfzaznuzxcidcfveihvhkfemikbwkiiwvmaueixvfdqsplfqlgfjxkfwxehislwokgsissfhzzvhhmxvwkihhimmexwsxcxyyfskvmegsqfzwfgwgjtslbsnixsdylgljknujlwdrgikkinwzifgjvfzfalmzwjixgvhmuutdiolrnqgyaivfugramuyfliislazlsiskjsqeoxvhlasi"

######################################################################
def get_factors(x):
   # This function takes a number and prints the factors
   res = []
   for i in range(1, x + 1):
       if x % i == 0:
           res.append(i)
   return res
#####################################################################
######################################################################
def get_nGrams(ctext, n):
   res = []
   i = 0
   while i<len(ctext):
   		x = ctext[i: i+n] +"---" + str(ctext.count(ctext[i: i+n]))
   		if x not in res and ctext.count(ctext[i: i+n])>2:
   			res.append(x)
   		i = i+1
   return res
##################################################################### get lengths between nGrams 

nGramLen = 3
nGram = get_nGrams(ciphertext, nGramLen)
print(nGram)


val = ciphertext.split("lfq")
print("val", val)
lengths = []

for x in val:
	if x != val[len(val)-1] and x != val[0]:
		lengths.append(len(x) + nGramLen)
print("lengths:", lengths)

################################################################# gets factors and common factors
factors = []
for y in lengths:
	factors.append(get_factors(y))

print("factors:", factors)

commonFactors = list(set(factors[0]).intersection(factors[1]))
print("commonFactors: ", commonFactors)

##########################################################################reorganzies in array by common factor length
n = 7
print('\n\n\nAssumed Key Length: ',n)
mapper = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]
print("\nMapper: ", mapper)
############################################################################## organize arrays by column

def colOrder(size, arr):
	colArr = []
	for i in range(0, size):##foll arr empty initial
		colArr.append([])
	for i in range(0, len(arr)):##traverse through each nGram in arr
		for j in range(0, len(arr[i])):##traverse through each column letter in arr[j]
			colArr[j].append(arr[i][j])
	return colArr
###########################################################################################get letters by column

colArr = colOrder(n, mapper)
print("\ncolumn array:")
for i in range(0, len(colArr)):
	print("-----------------------------------------------------------COL", i,"\n", )
	print(colArr[i])
	print("\nMost Common: ", collections.Counter(''.join(colArr[i])).most_common(1)[0], "\n")
print("-----------------------------------------------------------" )
#################################################################################
#################################################################################
commonLetters = [['e'], ['t', 'a','o' 'i', 'n', 's', 'h', 'r'], ['d','l'],['c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b']] 
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def deCryptByE(shift, arr):
	plainArr = []
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range(0, len(arr)): ##iterate through all letters
	    plainLetterLoc = alphabet.index(arr[i])-shift
	    if (plainLetterLoc<0):
	    	plainLetterLoc = len(alphabet) + plainLetterLoc
	    plainLetter = alphabet[plainLetterLoc]
	    plainArr.append(plainLetter)
	return plainArr
#################################################################################
def deCryptStep(colNumber, currentLetter, expected,currSentence, alphabet, currKey):
	columnNumber =colNumber 
	e_ciphered = currentLetter
	shiftRight = (alphabet.index(e_ciphered) - alphabet.index(expected))%26
	keyLetter = alphabet[shiftRight]
	currKey[colNumber] = keyLetter


	#print(keyLetter)
	#print(colArr[columnNumber])
	deCrypted1 = deCryptByE(shiftRight, colArr[columnNumber])
	#print(deCryptByE(shiftRight, colArr[columnNumber]))

	for i in range(0, len(colArr[columnNumber])):
		currSentence[(i*7)+columnNumber] = deCrypted1[i]
	print(''.join(currSentence))
	print('\n\n Key: ', currKey)
#################################################################################


sentenceArr = ["*"]*len(ciphertext)
currentKey = ['*','*','*','*','*','*','*']
#look at column with highest number of common occurence and its corresponding cipher letter
deCryptStep(1, 'i', 'e',sentenceArr, alphabet, currentKey)
deCryptStep(0, 'l', 't',sentenceArr, alphabet, currentKey)
deCryptStep(2, 'z', 'e',sentenceArr, alphabet, currentKey)
deCryptStep(6, 'a', 'i',sentenceArr, alphabet, currentKey)
deCryptStep(3, 'v', 'r',sentenceArr, alphabet, currentKey)
deCryptStep(4, 'v', 'e',sentenceArr, alphabet, currentKey)
deCryptStep(5, 'q', 'w',sentenceArr, alphabet, currentKey)


################################################################################# *h can be th, find the value for t

# columnNumber =0 
# e_ciphered = 'l'
# shiftRight = (alphabet.index(e_ciphered) - alphabet.index('t'))%26
# keyLetter = alphabet[shiftRight]


# print(keyLetter)
# print(colArr[columnNumber])
# deCrypted1 = deCryptByE(shiftRight, colArr[columnNumber])
# print(deCryptByE(shiftRight, colArr[columnNumber]))


# for i in range(0, len(colArr[columnNumber])):
# 	sentenceArr[(i*7)+columnNumber] = deCrypted1[i]
# print(''.join(sentenceArr))

# ################################################################################# col3, get word 'the'

# columnNumber =2 
# e_ciphered = 'z'
# shiftRight = (alphabet.index(e_ciphered) - alphabet.index('e'))%26
# keyLetter = alphabet[shiftRight]


# print(keyLetter)
# print(colArr[columnNumber])
# deCrypted1 = deCryptByE(shiftRight, colArr[columnNumber])
# print(deCryptByE(shiftRight, colArr[columnNumber]))


# for i in range(0, len(colArr[columnNumber])):
# 	sentenceArr[(i*7)+columnNumber] = deCrypted1[i]
# print(''.join(sentenceArr))




