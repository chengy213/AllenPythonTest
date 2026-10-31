import json

class User:
    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age}, email={self.email!r})"

data = '{"name": "allen", "age": 25, "email": "allen@example.com"}'
d = json.loads(data)                    # 先转成 dict
user = User(**d)                        # 用 ** 解包传给构造函数
print(user)                             # User(name='allen', age=25, email='allen@example.com')
