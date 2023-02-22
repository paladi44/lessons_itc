#цикл
#for
# while
a = [1,2,3,4,5,6,7,8,9]
b = 0
for i in a:#цикл
    b += i
    print(i)
print(b)


# a = [1,2,3,4,5,6,7,8,9]
# b = 0
# for i in a: # цикл 
#     if i == 5:
#         print('break')
#         break # остановк цикла
#     b += i
#     print(i)
# print(b)

# b = 0
# for i in range(1, 100000):#range
#     if i % 3 == 0 or i % 5 == 0:
#          b += i 
# print(b)         



# a = [5,2,7,65,75,25,0,6,5,6,8,4]

# mx = a[0]
# for i in a:
#     if i >= mx:
#         mx = i
# print(mx)        



# n = 0
# for i in range(10+1):
#     if i == 5:
#         n += i
#     print(n)   



# a = {'key': 'value', 'name': 'alex'}
# for i in a: 
#     if i == 'name':
#         print(a [i])
#         print(i, a[1])


# i = 0
# while i <= 0:
#     print(i, 'hello world')
#     i = i + 1
    




# password1 = input('enter pass')
# password2 = input('enter pas')
# i = 0
# while  password1 != password2:
#     i += 1
#     if i == 5:
#         print ('повторите попытку')
#         break
#     print ('пароли не совпали потворите еще раз')
#     print ('у вас осталось попыток :{5 - i}!')
#     print ('пароли не совпали')
#     password1 = input('enter pas')
#     password2 = input('enter pas')
# else:
#     print('done')



# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']   
# while lang1 in  languages:
#     print('есть в списке')
#     break
# else:
#     print('нет в списке')


# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']  
# for i in languages:
#     if i == 'php':
#         print (i)
#         break
#     else:
#         print('ненайдено')    
# умножить 7 на саму себя 7 раз

# i = 1
# n = 7
# while i < 7:
#     print (n)
#     i = i + 1
#     n = n*7
    
    
    #  Напишите код, который выведет на экран список языков с нумерацией.
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# Вывод:
#  0 go
#  1 java
#  2 php
#  3 python
#  4 javascript
#  5 ruby


languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
b = 0
for i in languages:
    print(languages.index(i),i)


# 5. Напишите цикл который выведет на экран:     1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1
# Усиловие:
# Получите такой же результат но с ОДНИМ циклом

five = [1,2,3,4,5,6,7,8,9,10,]
for i in five:
    print(five.index(i))


    
    
