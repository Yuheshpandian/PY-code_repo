
#avengers dict containing their names & character
avengers = {'iron_man':['funny','genius','brain','videogames','yes'],
'captain':['calm','talanted','strenght','outdoor sports','no'],
'thor':['serious','powerful','war weapon','videogames','yes'],
'spiderman':['funny','genius','brain','indoor sports','no'],
'hulk':['serious','powerful','strenght','outdoor sports','yes']}

print('WHICH AVENGER ARE YOU')

#users character
user_char = []

user_char.append(input('what type of person you are(funny,calm,serious): '))
user_char.append(input('what people think about you(genius,powerful,talanted): '))
user_char.append(input('what would you choose as your weapon(brain,strenght,war weapon): '))
user_char.append(input('what kind of games you like(videogames,outdoor sports,indoor sports): '))
user_char.append(input('do you like to use weapons that can kill others(yes/no): '))

#checks whether the lists are same or not
def same(list1,list2):
	for x in range(5):
		if list1[x] != list2[x]:
			return False
	return True
#func of the code
def mainfunc(dict,user_char):
	for avenger,char in dict.items():
		count = 0
		if same(char,user_char):
			return (f'you are like the avenger {avenger}')

	else:
		return 'you are a avenger on your on way'


print(mainfunc(avengers,user_char))
