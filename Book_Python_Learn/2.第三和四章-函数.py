#函数
# def hello():
#     print('Howdy!')
#     print('Howdy@')
#     print('Hello there.')
# hello()
#
# def hello(name):  #name是一个变元 相当于变量
#     print('Hi '+name)
#
# hello('Bob')
# hello('Job')
#
# #return 返回值
# import random
# def getAnswer(answerNunber):
#     if  answerNunber == 1:
#         return 'It is certain'
#     if  answerNunber == 2:
#         return 'It is decideddly so'
#     if  answerNunber == 3:
#         return 'Yes'
# bb =  getAnswer(answerNunber=10)
# print(bb)

#猜字小游戏
#This is a guess the number game.
# import random
# secretNumber =random.randint(1,20)
# print('I am thinking of a number between 1 and 20.')

#Ask the player to  guess 6 times.
# for guessTaken in range(1,7):
#     print('Taken guess.')
#     guess = int(input())
#
#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high.')
#     else:
#         break #This condition is the correct guess!
#
# if guess == secretNumber:
#     print('Good job! Your guessed my number in ' + str(guessTaken) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))

#这个程式很绝妙的通过for循环 因此打出了列表种的序列号和对应的值
supplies = ['pens','staplers','flame-throwers','binders']
for i in range(len(supplies)):
    print('Index '+str(i)+' in supplies is '+ supplies[i])














