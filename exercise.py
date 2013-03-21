###########################################################

# exercise 1

def print_name(name):
	print 'your name is :\n', name

	
def print_rename(name1, name2):
	print_name(name1)
	print 'he is from ' + name2 + ' family'

print_rename('sunjin', 'choi')

###########################################################

###########################################################

# exercise 1-add

#print_rename_add('sunjin', 'choi')
#
#def print_name_add(name):
#	print 'your name is :\n', name
#
#	
#def print_rename_add(name1, name2):
#	print_name_add(name1)
#	print 'he is from ' + name2 + ' family'

###########################################################

###########################################################

# exercise 2

def ab() :
	num = input ( "input number : " )
	if ( 0 > num ) :
		print num
	else :
		print -num

ab()
	
###########################################################

###########################################################

# exercise 3

def change() :
	num = input( "input number : " )
	if( 0 <= num <= 10 ) :
		print num + 10
	elif( 10 <num<= 100 ) :
		print num * 0.1
	else :
		print False

change()

###########################################################

###########################################################

# exercise 4
	
def dist() : 
	import math
	x1,y1,x2,y2 = input( "input coodinate(x1,y1,x2,y2): " )
	
	dx = x2 - x1
	dy = y2 - y1
	
	dist = math.sqrt( dx ** 2 +  dy ** 2 )
	print dist

dist()

###########################################################

###########################################################

# exercise 5

def count() :
	i = 0
	for str in "next people":
		if ( str == 'e' ) :
			i += 1
	print "the number of i :", i
		
		
count()

###########################################################

###########################################################

# exercise 6

def mir() :
	word = raw_input( "Input a word : " )
	i = 0
	check = 0
	l = len ( word )
	while ( i < l/2 ) :
		a = word[ i : i+1 ]
		b = word[ l-i-1 : l-i ]
		print "compare", a,",", b
		i += 1
		if ( a != b ) :
			check += 1
	if ( check == 0 ) : 
		print "same"
	else :
		print "different"

mir()

###########################################################





		
	

