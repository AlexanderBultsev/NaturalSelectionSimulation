import random

from individual import Individual


class Predator(Individual):
    def __init__(self, field, max_age, min_reproduction_age, max_reproduction_age, fertility, consumption, viability,
                 position_x, position_y):
        """
        :param field: Field object
        :param max_age: age in days
        :param min_reproduction_age: age in days
        :param max_reproduction_age: age in days
        :param fertility: number of hares per day
        :param consumption: consumption per day
        :param viability: number of days before death
        :param position_x: x position on field
        :param position_y: y position on field
        """
        super().__init__(field, max_age, min_reproduction_age, max_reproduction_age, fertility, consumption, viability,
                         position_x, position_y)

    def eat(self):
        for individual in self.field.individuals:
            if individual != self:
                if individual.position_x == self.position_x and individual.position_y == self.position_y:
                    self.field.remove(individual)
                    self.satiety = 1.0
                    return

    def reproduce(self):
        if self.min_reproduction_age <= self.age <= self.max_reproduction_age:
            if self.health * self.fertility > random.random():
                self.field.add(Predator(self.field, self.max_age, self.min_reproduction_age,
                                        self.max_reproduction_age, self.fertility, self.consumption, self.viability,
                                        self.position_x, self.position_y))
