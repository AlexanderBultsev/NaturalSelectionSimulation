import random


class Individual:

    def __init__(self, field, max_age, min_reproduction_age, max_reproduction_age, fertility, consumption, viability,
                 position_x, position_y):
        """
        :param field: Field object
        :param max_age: age in days
        :param min_reproduction_age: age in days
        :param max_reproduction_age: age in days
        :param fertility: number of hares per day
        :param consumption: supply consumption per day
        :param viability: number of days before death without supply
        :param position_x: x position on field
        :param position_y: y position on field
        """
        self.field = field
        self.max_age = max_age
        self.min_reproduction_age = min_reproduction_age
        self.max_reproduction_age = max_reproduction_age
        self.fertility = fertility
        self.consumption = consumption
        self.viability = viability
        self.position_x = position_x
        self.position_y = position_y
        self.age = 0.0
        self.satiety = 1.0
        self.health = 1.0
        self.decay = 0.0

    def move(self):
        self.position_x = max(min(self.position_x + random.randint(-1, 1), self.field.max_x), self.field.min_x)
        self.position_y = max(min(self.position_y + random.randint(-1, 1), self.field.max_y), self.field.min_y)

    def eat(self):
        if self.field.supply >= self.consumption:
            self.satiety = 1.0
        self.field.supply = max(0.0, self.field.supply - self.consumption)

    def reproduce(self):
        if self.min_reproduction_age <= self.age <= self.max_reproduction_age:
            if self.health * self.fertility > random.random():
                self.field.add(Individual(self.field, self.max_age, self.min_reproduction_age,
                                          self.max_reproduction_age, self.fertility, self.consumption, self.viability,
                                          self.position_x, self.position_y))

    def death_rate(self):
        # теоретически, параметр 'a' зависит от распределения случаев смерти по оси возраста
        a = 0.001
        return a ** (1 - self.age / self.max_age)

    def survive(self):
        # теоретически, параметр 's' зависит от уровня удовлетворенности особи сытостью
        s = 0.5
        # надо доработать вред 'harm', не понимаю от чего он зависит
        # надо доработать разложение 'decay', оно слишком быстрое
        harm = 1.0 / self.viability
        if self.health < 0.0:
            self.health = 0.0
            self.decay += harm
            if self.decay > 1.0:
                self.field.remove(self)
        else:
            if self.death_rate() > random.random():
                self.health = 0.0
                return
            self.health = min(self.health + harm * (self.satiety - s), 1.0)
            self.satiety = max(0.0, self.satiety - harm)
            self.age += 1
            self.move()
            self.eat()
            self.reproduce()

    def __str__(self):
        return (f'{self.__class__.__name__}[age: {self.age}, satiety: {self.satiety}, health: {self.health}, '
                f'decay: {self.decay}, x: {self.position_x}, y: {self.position_y}]')
