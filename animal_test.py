class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Toy(object):
    def run(self):
        print('Toy is running...')

def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Toy()))

class Counter:
    count = 0                 # 类变量

    def __init__(self):
        Counter.count += 1    # 通过类名修改

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count)          # 3，所有实例共享