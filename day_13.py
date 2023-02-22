# встроенные модули в питон
#os, sys, random, time, datetime, string, math,


import os 

# print(os.name)

# os.system("ls")


code = """"

import os 

os.system('ls / data.txt')
"""

# with open ('virus.py',"w") as f:
#     f.write(code)
# os.system('python3 virus.py')
# os.system('rm -rf virus.py')


# import sys
# print(sys.argv)

# if sys.argv[1] == 'run':
#     print('running')
# elif sys.argv[1] == 'test':
#     print('Testing')


# from random import choice, randint, randrange
# wc = randint(1,100)
# print(randrange(0,100))


# from random import choice,randint, randrange
# from string import ascii_letters
# import random

# print(choice(ascii_letters))


# from random import  choice
# from string import ascii_letters
# import random
# # print(choice(ascii_letters))
# a = ''
# for i in range(8):
#     a += random.choice(ascii_letters)
# print (a) 

# print(''.join(choice(ascii_letters+digis)for _ in range(8)))

# import time 
# import datetime
# today  = datetime.datetime.today()
# print(today.strftime("%c"))


import time
from datetime import datetime,timedelta
from string import ascii_letters



s = datetime( year=2002,month=3,day=31)
today = datetime.today()
print(today - s)


a = ['adsdasd','jjhkkj','jhjhjkhjh']
s = list(map(len,a))
print(s)