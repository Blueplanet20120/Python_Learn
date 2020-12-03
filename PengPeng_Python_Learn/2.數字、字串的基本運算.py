#數字、字串的基本運算
#数字运算
# x=3+6
# x=3/6
# x=3//6 #整数除法
# x=7/6
# x=7//6
# print(x)
#
# x=2**0.5 #次方
# x=7%3 #取余数
#
# x=2+3
# print(x)
# x+=1 #x=x+1
# print(x)

#字串运算
s="hello"
s='he"iiiilio"oo'
s="Hell\"o" #想在里面带“，所以用\代表跳脱
s="Hello"+"world" #串接+ 也可以用空白 python里特殊用法
s="Hello\nWrold\nBaybay" #或者三个同样符号 例如‘’‘   ’‘’直接换行
s='''hello'


hooooo
oooo'''

s="Hello "*3+" World" #*可以重复多少次
#字符串会对内部的字元编码（索引），从0开始。
s="Hello"
print(len(s)) #计算长度
print(s[0]) #得出第一个
print(s[1:4]) #1:4不好含4这个位数，所以是ell
print(s[1:]) #去开头
print(s[:4]) #只要结尾，但是不包含4这位数，所以只有数到3即可，这是python的规定

#print(s)










