# 亂數與統計模組
# 随机模组
import random

# 随机选取
data = random.choice([1, 5, 7, 8, 9, 12, 44])
data = random.sample([1, 5, 7, 8, 9, 12, 44], 3)  # 随机选择3个
print(data)
# 随机调换顺序（就是洗牌的概念）
data = [1, 5, 8, 20, 34, 5, 66, 60]
random.shuffle(data)
print(data)
# 随机选取乱数
data = random.random()  # 0~1之间的随机乱数
#相当于：
data = random.uniform(0.0,1.0)
print(data)
#取得常态分布乱数
data=random.normalvariate(100,10) #平均数100，标准差10，得到的资料多数在90-110之间
print(data)
#平均数0 ，标准差5，得到的资料多数在-5 ~ 5 之间
data=random.normalvariate(0,5)
print(data)

#统计模组
import  statistics as stat
data=stat.mean([1,4,5,8]) #平均数
data=stat.median([1,2,3,4,5,6,7,100]) #中位数
data=stat.stdev([1,2,3,4,5,6,7,21]) #标准差 代表资料的散布状态
print(data)

#网络上了解：平均数 中位数 标准差 常态分布
