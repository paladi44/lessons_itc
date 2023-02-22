# d = []
# a = (*s, *r )
# * -argi ("распаковывает все массивы")
# типы данных 
# изменяемые - list set dict
# НЕ изменяемые - int float bool string tuple



# # Множество № 1:
# dates_of_birth = {3,10,11,7,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)


# # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# c =  farm_1.intersection_update(farm_2)
# print(c)

# farm_2 = {"dog", "cat", "mouse", "sheep"}
# farm_3 = {"cow", "horse", "donkey", "cat", "dog"}
# j = farm_3.difference(farm_2)
# print (j)


# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_2.add("mouse",) #добавить в сет значение
# print (farm_2)
# farm_2.pop()
# print (farm_2)

 # Словарь №1:
# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# menu.update({"besh": 130}) # добавить или изменить индекс в {сет } 
# menu.update({"besh": 135 }) 

# menu['besh'] = 130 #добавить в {сет} 
# menu.pop("borsh") #удалить из {сет}
# print(menu)

# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# drinks = {'drinks':['coca','sprite', 'fanta']}
# menu.update(drinks)
# print (menu)
# print(menu['drinks'][1])

# comand_set = {'add', 'remove','clear','update','difference','discard','intersection','pop'}
# command_dict = {'clear','keys','get','values','items','update'}
# comand_set.intersection('command_dict')
# print (comand_set)


# libary = {}
# a = print({input('login')})
# b = print({input('pssword')})
# c = ['a','b']
# libary.update([c])
# print(libary)


dann = (3,10,11,7,31,21,1,10,3,5,6,6)
