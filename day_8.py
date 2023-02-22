# file = open('tst.txt', 'w')  #ОТКРЫВАЕМ ФАИЛ 
# text = 'Hello, world'
# file.write(text) #принимает отльок один аргумент
# file.close() #закрываем фаил 

# file = open('tst.txt', 'w')  #ОТКРЫВАЕМ ФАИЛ 
# s = '\n'
# for i in range(10):
#     s += str(i)  #добовляем тольок инт
# file.write(s)
# file.close()


# file = open('files.txt', 'r')
# text =  file.read().split('\n')
# h = 0
# for i in text:
#     if i.startswith('day') and i.endswith('py'):
#         h  += 1

# if i.find('day') >= 0:
#     h += 1

# if i[3:6] == "day":
#     h += 1

# if 'day' in i:
#     h += 1

# print(h)




# with open('files.txt', 'r') as d:
#     text = d.read().splitlines()
#     for i in text:
#         print(i)  


# user = input( "log ")
# password = input ("password")
# with open ('users.txt', 'w') as f:
#     text = f"login:{user} password = {password}"
#     f.write(text)
with open ('files.txt', 'r') as t:
    a  = t.read()
    if "w" in a:
        print ("да в тексте есть w ")
    else: 
        print( 'нет  в тексте нет w')


