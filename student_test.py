import dataclasses
from itertools import count
from enum import Enum
from dataclasses import dataclass, field

class MY_GENDER(Enum):
    GIRL=0
    BOY=1
class Student(object):
    count=0

    def __init__(self, name, gender, score:int, city="hz"):
        if gender not in MY_GENDER:
            raise ValueError("error gender!")
        self._gender=gender
        self._name=name
        self._score=score
        self.__city=city
        Student.count+=1
    def print_score(self):
        print(f"name={self._name},gender={self._gender},score={self._score},city={self.__city}")
    def get_city(self):
        return self.__city

s1=Student("allen", MY_GENDER.BOY, 35)
s2=Student("frank", MY_GENDER.BOY, 30)
s3=Student("andy", MY_GENDER.GIRL,40)

s1.print_score()
s2.print_score()
s3.__city="sh"
s3.print_score()
print(s3.get_city())

print(s3.count)

@dataclass
class User:
    name: str = ''

u1=User()
u1.name="123"
print(u1)

class Screen(object):
    def __init__(self, width, height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return f"resolution={self._width} x {self._height}"

screen1=Screen(500, 200)
print(screen1.resolution)

class Chain(object):
    def __init__(self, path=''):
        self._path=path

    def __getattr__(self, path):
        return Chain(f"{self._path}/{path}")

    def __call__(self, param):
        """处理带参数的调用，如 users('michael')"""
        return Chain(f"{self._path}/{param}")

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().users('michael').repos)