import pandas as pd

df = pd.read_csv('./athlete_events.csv')

#Задание 1
femaleAge = df[(df['Sex'] == 'F') & (df['Year'] == 1996)]['Age'].min()
maleAge = df[(df['Sex'] == 'M') & (df['Year'] == 1996)]['Age'].min()
print(femaleAge, maleAge)

#Задание 2
maleGymnasts = df[(df['Sex'] == 'M') & (df['Year'] == 2000)].drop_duplicates(subset=['Name']).value_counts(subset=df['Sport'] == 'Gymnastics', normalize=True)
print('{:.2%}'.format(maleGymnasts[True]))

#Задание 3
femaleBasketball = df[(df['Sex'] == 'F') & (df['Sport'] == 'Basketball') & (df['Year'] == 2000)]['Height'].describe()
print(femaleBasketball['mean'], femaleBasketball['std'])

#Задание 4
heavyOne = df.loc[df[df['Year'] == 2000]['Weight'].max()]
print(heavyOne['Sport'])

#Задание 5
personPawBratkiewicz = df[df['Name'] == 'Paw Bratkiewicz'].count()
print(personPawBratkiewicz['ID'])
personPaweAbratkiewicz = df[df['Name'] == 'Pawe Abratkiewicz'].count()
print(personPaweAbratkiewicz['ID'])

#Задание 6
silverMedalsAustralia = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Tennis') & (df['Year'] == 2000) & (df['Medal'] == 'Silver')].count()
print(silverMedalsAustralia['ID'])

#Задание 7
medalsSwitzerland = df[(df['Team'] == 'Switzerland') & (df['Year'] == 2016) & (df['Medal'].notna())].count()
medalsSerbia = df[(df['Team'] == 'Serbia') & (df['Year'] == 2016) & (df['Medal'].notna())].count()
if medalsSwitzerland['Medal'] > medalsSerbia['Medal']:
    print(True)
else:
    print(False)

#Задание 8
from15to25 = df[(df.Age >= 15) & (df.Age < 25) & (df['Year'] == 2016)].drop_duplicates(subset=['Name']).count()
from25to35 = df[(df.Age >= 25) & (df.Age < 35) & (df['Year'] == 2016)].drop_duplicates(subset=['Name']).count()
from35to45 = df[(df.Age >= 35) & (df.Age < 45) & (df['Year'] == 2016)].drop_duplicates(subset=['Name']).count()
from45to55 = df[(df.Age >= 45) & (df.Age < 55) & (df['Year'] == 2016)].drop_duplicates(subset=['Name']).count()
ages = {from15to25['ID']: 'от 15 до 25', from25to35['ID']: 'от 25 до 35', from35to45['ID']: 'от 35 до 45', from45to55['ID']: 'от 45 до 55'}
print('Минимальное количество в возрасте '+ages[min(ages)]+'. Максимальное количество в возрасте '+ages[max(ages)])

#Задание 9
if True in df.City.str.contains('Lake Placid').to_dict().values():
    print(True)
else:
    print(False)

if True in df.City.str.contains('Sankt Moritz').to_dict().values():
    print(True)
else:
    print(False)

#Задание 10
sport1996 = df[df['Year'] == 1996]['Sport'].drop_duplicates().count()
sport2016 = df[df['Year'] == 2016]['Sport'].drop_duplicates().count()
print(abs(sport1996 - sport2016))

#Задание 12
dups = df.pivot_table(index=['Name'], aggfunc='size')