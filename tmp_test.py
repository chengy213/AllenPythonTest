users = [{"name": "张三", "age": 20}, {"name": "李四", "age": 15}]
adult_names = [u["name"] for u in users if u["age"] > 18]
name_age = {u["name"]: u["age"] for u in users}
print(type(adult_names))
print(type(name_age))
print(name_age)