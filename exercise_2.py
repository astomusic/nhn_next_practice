"""
num = [3,7,4,5]
num.append(6)
print num

num.sort()
print num

new_num = num.sort()
print new_num

new_num = num.sorted(iterable[, cmp[, key[, reverse]]])
print new_num


def del_list(list2) :
	del list2[0]

letter = [ 'a', 'b', 'c' ]
del_list(letter)
print letter
print letter[0] 
print list2


classes = {'1.mon' : ['Inmon'], '2.tue' : ['Algorism', 'English', 'Critical'], '3.wed' : ['Programming','Design project'], '4.thur' : ['Algorism','UX','NEXT','STAT'], '5.fri': ['Algorism','Math'] }

for a in classes :
	print a, ":", classes[a]

people = {'minsu' : 43 , 'jisu':33 , 'john' : 21 , 'david' : 33, 'hary':36, 'messi' :33, 'ronaldo' : 27}
people_age = { '20s' : [] , '30s' : [] }


for i in people :
	if people[i] >= 30 and people[i] < 40 :
		people_age['30s'].append(i)
	if people[i] >= 20 and people[i] < 30 :
		people_age['20s'].append(i) 

print people_age
"""		


people = {'minsu' : 43 , 'jisu':33 , 'john' : 21 , 'david' : 33, 'hary':36, 'messi' :33, 'ronaldo' : 27}
people_age={}
 
for i in people :
	gen = int(people[i] / 10) * 10
	tempstr = '%ds'%gen
	if (tempstr) not in people_age :
		people_age[tempstr]=[]
	people_age[tempstr].append(i) 

print people_age


