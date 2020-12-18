#類別的定義與使用
#定義類別IO,有兩個屬性 supportedSrcs read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("NOT Supported")
        else:
            print("Read frome",src)
#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("rr")