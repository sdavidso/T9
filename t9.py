#import marisa_trie
import sys

#dictionary's data structure, uses a memory-efficient trie
#to store words
#trie = marisa_trie.Trie()
trie = [];
DIR = "./scowl-7.1/final/" #directory for word list

#dictionary storing the possible letters per number press
NMAP = ({ 0 : [],
	    1 : [], 
	    2 : ['a','b','c'],
	    3 : ['d','e','f'],
            4 : ['g','h','i'],
            5 : ['j','k','l'],
            6 : ['m','n','o'],
            7 : ['p','q','r','s'],
            8 : ['t','u','v'],
            9 : ['w','x','y','z']
	})

#checks all possible combinations for matches
#FIX ME
def checkAll(lis):
	tmp = []
	for a in lis:
		if a in trie:
			tmp.append(a)
	tmp.sort()
	return tmp		

#this takes an inputted number and outputs a list of all
#letter combinations
def parseAll(num):
	return recfun([],num)

#FIX ME
#reversed, not saving lesser characters
def recfun(lis,num):
   tmp = [];
   if num == 0:
	return lis
   else:
	if lis != []:
		for x in lis:
			for y in NMAP[num%10]:
				tmp.append(y+x)
	else:
		tmp = NMAP[num%10]
   return recfun(tmp,num/10)


#fills in data structure with possible words
def createDict():
   for a in range(1,20):
	   try:
   		f = open(DIR + "english-words."+str(5*a),'r') #open word list
   		for word in f.readlines():
			trie.append(word.strip());
   	   except: pass

def main(argv):
   createDict();
   pA = parseAll(int(argv[1]))
   #print "parse all: completed" 
   #print "check all: " , checkAll(pA)
   print checkAll(pA)

# start
if __name__ == "__main__":
   main(sys.argv)
