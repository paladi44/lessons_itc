# add()
# substract()
# multyply()
# divide()

# def add(a, b):
#     return (a+b)

# print(add(2,3))

# def substract (a, b):
#     return (a-b)
# print(substract())


# def multyply(a,b):
#     return (a*b)
# print (multyply())

# def divide(a,b):
#     return(a/b)
# print (divide())






# def lenght(a):
#     b = 0
#     for i in a:
#         b += 1
#     return b


# a = input()   
# print(lenght(a))
# a = {'sons': 'root'}
# b = {'red': 'talk' }
# def plusdict(a, b):
#     c = b.update(a)
#     return c
# print (plusdict(a, b))

# a = input()
# def whateat(text):
#     with open ('menu.txt',"a") as f:
#         f.write('\n'+text)
        
# print(a)
# whateat(a)

# name = input()
# def rename(text):
#     with open ("name".txt, 'a') as f:
#         f.write()
# print(name)
# //

def decor (func):
    def wrapper (*args, **kwargs):
        return func (*args, **kwargs)
    return wrapper

@decor 
def main (*args, **kwargs):
    return sum(args), kwargs

n = map(int, input('>>').split())
n = [1,2,3,45,6,7,8]    
print (main(*n, name = 'decor'))
