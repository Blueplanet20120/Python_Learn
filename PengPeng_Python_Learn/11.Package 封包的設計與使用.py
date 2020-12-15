# Package 封包的設計與使用
#调用封包
import geometry.point #完整载入封包模组
result=geometry.point.distance(3,4)
print("距离",result)
import geometry.line as line
result=line.slope(1,2,3,4)
print("斜率",result)