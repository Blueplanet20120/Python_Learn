#*args
def add(num1,num2):
    print(num1+num2)
add(1,1)

#如果再有更多的参数需要相加，就需要*args
def add(*args):
    print(sum(args))
add(1,1,2,2,2)