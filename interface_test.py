from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def run(self):
        """子类必须实现"""
        pass

    @abstractmethod
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def run(self):
        print("Dog runs")

    def eat(self):
        super().eat()
        print("Dog eats")

Dog().eat()