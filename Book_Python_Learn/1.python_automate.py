#快速上手
# print(len('hhhhh')) #len()只能计算字符串或者字符串变量的长度，因此里面必须是string
# myName = input('pleas you name:')
# print('你的名字是：'+myName)
# print('你的名字有'+str(len(myName))+'位') #中间要加入str() 因为字符串只能盒字符串连接

# name = ''
# while name != 'liusong':
#     print('输入有误,请输入管理员的名字:\n')
#     name = input()
# print('-'*20+'回答正确'+'-'*20)
# print('thanks')

# while True:
#     print('please type your name')
#     name = input()
#     if name != 'liusong':
#         continue
#     print('please type your password')
#     passwd = input()
#     if  passwd == 'passwd':
#         break
# print('access granted.thank your')

# for i in range(3,20,3): #range可以有三个参数,第三个数字是"步长",step
#     print(i)
# for i in range(5,-1,-1): #递减,递减率为-1
#     print(i)
#
#
# spam+1=spam

# import random,sys,os,math
# while True:
#     print('hhhhhh')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('you typed ' + response + '.')

#做出两个while 和 for 相等的 表达(1-10)的数字显示出来
#while:
spam=1
while spam<=10:
    print(spam)
    spam = spam + 1
print('*'*30+'one day lesson'+'*'*30)
#for:
for i in range(1,11):
    print(i)

