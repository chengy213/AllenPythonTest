# Iterator (迭代器) 只能遍历一次
it = iter([1, 2])
for i in it: print(i)  # 输出 1, 2
print("-----")
for i in it: print(i)  # 什么都不输出 (因为迭代器已经空了)
