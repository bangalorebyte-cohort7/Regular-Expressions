import re 

# string matching without regular expressions

"""text = open("melville-moby_dick.txt")
for line in text:
	#strip() removes characters from the beggining and end of string 	
	line = line.strip() 
	word = 'lexicons'
	if line.find(word[:-1]) >=0:
		print(line)

# using regex
for line in text:
	line = line.strip()
	#search() finds only the first occurrence of the pattern within the string.
	if re.search('lexicon',line):
		print(line)
# find line that starts with lexicon
for line in text:
	line = line.strip()
	if re.search('^lexicon',line):
		print(line)"""

#find any string that starts with X followed by any character
word1= "X-Sieve: CMU Sieve 2.3"
word2 = "X-DSPAM-Result: Innocent"
word3 = "X-Plane is behing schedule: two weeks"


print(re.search('^X-.*[0-9]',word3))


# lets look at a more complicated example

#find any string that matches a string begging with 'X-' followed by no whitespace and one or more characters

text1 = "My 2 favorite numbers are 19 and 42"
re = re.findall('[0-9]+',text1)
print(re)
