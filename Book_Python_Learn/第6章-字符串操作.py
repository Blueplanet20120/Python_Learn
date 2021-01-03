#双引号 单引号的混用
#转义符
# \'
# \"
# \t
# \n
# \\

#原始字符串 r 忽略所有转义符等 全部打印  正则表达式时候非常有用
# print(r'that is carol\'s cat')

#三重引号 都是很好的注释串
# print('''
# thh hh
# hhlso
# osoos
# ''')

#字符串下标和切片
# spam = 'Hello World!'
# print(spam[2])
# print(spam[:3])
# print(spam[2:])
#
# #字符串的in 和not in 操作
# print('Hello' in 'Hello World!') #True
# print('Hello' not in 'Hello World!') #False

#字符串方法 upper() lower() isupper() is lower()
#upper() lower() 转换大小写
#isupper() is lower() 如果字符串中至少有一个字母,并且所有字母都是大写或者小写,这两个方法返回True,否则返回False
# spam = 'Hello World!'
# print(spam.upper()) #HELLO WORLD!
# print(spam.lower()) #hello world!
# print(spam.isupper()) #False
# spam=spam.upper()
# print(spam.isupper())
# print(spam.islower())

#isX 字符串方法
# isalpha()返回True,如果字符串只包含字母,并且非空;
# isalnum()返回True,如果字符串只包含字母和数字,并且非空;
# isdecimal()返回True,如果字符串只包含数字字符,并且非空;
# isspace()返回True,如果字符串只包含空格/制表符/和换行/并且非空;
# istitle()返回True,如果字符串仅包含大写字母开头,后面都是小写字母的单词.

#有效示例:
# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')
# while True:
#     print('Select a new password (letters and numbers only')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers.')

#字符串方法startswith() endswith() 方法返回True,如果他们所调用的字符串以该方法传入的字符串开始或者结束.
spam = 'Hello World!'.startswith('Hello')
print(spam) # True

#字符串方法 join() split()
#如果有一个字符串列表,需要连接起来,成为一个单独的字符串,join()就很有用.参数是一个字符串列表,返回一个字符串.而split()刚好相反.
print(','.join(['cats','rats','bats'])) # cats,rats,bats
print(' '.join(['cats','rats','bats'])) # cats rats bats
print('ABC'.join(['cats','rats','bats'])) # catsABCratsABCbats
print('catsABCratsABCbats'.split('ABC')) # ['cats', 'rats', 'bats']
print('catsABCratsABCbats'.split('a')) # ['c', 'tsABCr', 'tsABCb', 'ts']


#一个常见的 split() 用法,是按照换行符分割多行字符串,如:
spam= '''Dear Alice,
How have you been? I am fine.
There is a container in the fridege
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n')) #换行符分割多行字符串
#['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the fridege', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 'Sincerely,', 'Bob']

#用rjust() ljust() center()方法对齐文本 分别是右 左 中间对齐方法.
spam='Hello World'
print(spam.rjust(20)) # 向右边移动20个空格
print(spam.rjust(20,'*')) # 以*字符向右边移动20个格
print(spam.center(20,'*'))


#用strip() rstrip() lstrip() 删除空白字符


#用pyperclip模块拷贝粘贴字符串
import pyperclip
pyperclip.copy('Hello World!')
pyperclip.paste()


















