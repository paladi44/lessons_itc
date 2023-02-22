# s = [3, 4, 2, 4, 5, 5, 5, 4]
# s.append(66)
# s.append(True)
# s.append([123,123])
# print(s)



# s = [1569,2,3,4,5,5,5, 4, 5, 4, 5, 4, 5, 4, 5]
# s.append(True)
# s.remove(1569)
# s.pop(0)
# print(s)


# s1 = [1569,2,3,4, 4, 5, 4, 5, 4, 5, 4, 5]
# s2 = [15, 4, 5, 4, 5, 4, 5, 12]

# s1.append(s2)

# # s1 += s2
# s1.extend(s2)

# s1.sort(reverse=True)

# print(s1)


# s1 = [1569,2,3,4, 4, 5, 4, 5, 4, 5, 4, 5]

# s1.reverse()
# print(s1)

# print(s1.count(4))

# a = (1, 2,'sdfkjhsdkjf',True,  4, 5, 5, 5, 5, 5, 5)


# print(a[2])
# b = []
# print(type(a))
# print(type(b))
# b = []
# b.extend(a)
# print(b)


# a = [1,2,3,3,4,5,7,8]
# print(a.index(7))

# a.reverse()
# print(a)
# print(a)
# print(a)

# print(a[3:6])
# print(a)

# a = []
# b = (11,22,33,44,55)
# c  = (1,2,3,4,5)
# d = (2,2,2,2)
# e = (5,5,5,5,5)
# a.append(b)
# a.append(c)
# a.append(d)
# a.append(e)
# print (a) 

# a = [1, 2, 3]
# print (a[0], a [1], a[2])

# a = [1,2,3]
# a.append(123)
# a.append(True)
# a.append(1.3)
# a.append ([123,123])
# print (a)

# name = ["rick", "morty", "yan",]
# b = ", "
# print( b.join(name))

# list_1 = [1, 2,3,4,5]
# list_2 = [6,7,8,9,10]
# b = list_1 + list_2
# print(b)
# list_1 = []
# list_2 = []


# a = int(input('>> '))
# b = int(input('>> '))
# c = int(input('>> '))
# d = int(input('>> '))
# e = int(input('>> '))


# if a % 2 == 0:
#     print("-") 
#     list_1.append(a)

# else:
#     print("+")
#     list_2.append(a)



# if b % 2 == 0:
#     print("-") 
#     list_1.append(b)

# else:
#     print("+")
#     list_2.append(b)

# if c % 2 == 0:
#     print("-") 
#     list_1.append(c)

# else:
#     print("+")
#     list_2.append(a)

# if d % 2 == 0:
#     print("-") 
#     list_1.append(d)

# else:
#     print("+")
#     list_2.append(d)

# if e % 2 == 0:
#     print("-")
#     list_1.append(e)

# else:
#     print("+")
#     list_2.append(e)
# print(list_1 )
# print(list_2)
# a = len(list_1)
# b = sum(list_1)
# c=b/a
# print(c)
# d = len(list_2)
# e = sum(list_2)
# f = e/d
# print(f)
# list = []
# aa = int(input("vvedite 5 chisel " ))
# list.append (aa)
# print(list)
# print ()

# products = [
#     'apple',
#     'watermalone',
#     'banan',
#     'mandarin',
#     'grusha'
# ]
# b = (", ")

# print( b.join(products))
# c = int(input('vybor: '))


# if c > 0 or c < 5:
#     products.pop(c - 1)
#     print("prod")
# else:
#     print("not vailed")
# """
# password
user = [('aktan2002', 'qwerty'),('ilim12', '12345')]
name = input('login >')

if name.isdigit() != True and name.isalpha() != True:
        print ('done ')
        password = input('password >')
        password2 = input ("repeat password >")
        if password == password2:
                print('welckom')
                cd = ( name, password)

                user.append(cd)
                print (user)
        else: 
                print ('povtor')
else:
        print ('dighit and alpha')
                
       