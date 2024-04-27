from herbivore import Herbivore
from predator import Predator


class Field:
    def __init__(self, configuration):
        self.min_x = configuration[0]
        self.max_x = configuration[1]
        self.min_y = configuration[2]
        self.max_y = configuration[3]
        self.supply = configuration[4]
        self.supply_recovery = configuration[5]
        self.individuals = []
        for herbivore in configuration[6]:
            self.add(Herbivore(self, *herbivore))
        for predator in configuration[7]:
            self.add(Predator(self, *predator))

    def add(self, individual):
        self.individuals.append(individual)

    def remove(self, individual):
        if individual in self.individuals:
            self.individuals.remove(individual)

    def __str__(self):
        return (f'Field [supply: {self.supply}, supply recovery: {self.supply_recovery},'
                f'individuals: {len(self.individuals)}]')