# a = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# a1 = set()
# a2 = []
# for i in a:
#     try:
#         a1.add(i)
#         a2.append(True)
#     except TypeError:
#         print (i)
#         a2.append(False)
# 
# print(all(a2))
# python
# try:
#     a = print(eval(input('>>')))
# except NameError:
#     print ('function is not')
# except SyntaxError:
#     print('function is not')    
##bank
# clients = int(input("vvedite summ "))
# while clients < 50000:
#     print ("not")
#     clients = int(input("vvedite summ "))


# else:
#     print ('ok')
#     print("pereplata",clients*(3.47/100))

# code2


 #1:

# at = 10
# in1 = 15
# wo = 20

# for e in range(-at, at):
#     try:
#         print(wo / e)
#     except ZeroDivisionError:
#         print("деление на ноль")
# if "at" > '5':
#     print ("at" > "5")
 #3:
# a = (0,)
# b = (1,)
# numbers = []
# while b > a:
#     numbers += b
# b += 1

#1:

# import abc


# dict_1 = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
# for i in dict_1.keys():
#     try:
#         print ('str in')
#     except TypeError:
#             print("int in spisok")
#     print (str(i) + "abc")
