from threading import Thread
from time import sleep

from field import Field


def simulation(configuration, log_enable=False):
    field = Field(configuration)
    day = 0
    while len(field.individuals):
        # можно попробовать обернуть в многопоточность
        # но пока выигрыша в скорости не заметил
        #
        # threads = []
        # for individual in field.individuals:
        #     thread = Thread(target=individual.simulate)
        #     thread.start()
        #     threads.append(thread)
        # for thread in threads:
        #     thread.join()
        #
        for individual in field.individuals:
            individual.survive()
        day += 1
        if log_enable:
            print(f'Simulation [day: {day}]')
            print(field)
            for individual in field.individuals:
                print(individual)
            sleep(1)
    return day
