#获取当前文件路径
print("#获取当前文件路径")
import os
import sys

if __name__ == "__main__":
    print("#当前的文件Linux格式路径为： ")
    sh_path = os.path.dirname(os.path.abspath(sys.argv[0])) #获取当前的win路径并转行为linux路径。
    #print(sh_path)
    sh_path = '/'.join(sh_path.split('\\'))  # transform the windows path to linux path
    print(sh_path)