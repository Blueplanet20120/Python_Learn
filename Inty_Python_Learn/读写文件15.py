#读写文件 with open() as f:)
# file=open('F:/Python_Learn/Inty_Python_Learn/venv/inty.txt') #注意，读取文件的路径和windows\不通，可以尝试用其他终端看看。
# text=file.read()
# file.close()
# with open('F:/Python_Learn/Inty_Python_Learn/venv/inty.txt','r', encoding='UTF-8') as f:
#     print(f.read())
# #写文件
# with open('inty.txt','w') as f:
#     f.write('hell world,i love u')


#'w' 之前的内容被覆盖，不被覆盖用‘
with open('F:/Python_Learn/Inty_Python_Learn/venv/inty.txt','a') as f:
    f.write('hell world,i love u\n')
