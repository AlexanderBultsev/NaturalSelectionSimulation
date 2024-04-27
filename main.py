from simulation import simulation

# основная задача - подобрать конфигурацию
configuration = [
    0, 20,
    0, 20,
    200, 1,
    [[7200, 0, 3600, 0.01, 0.5, 10, 5, 5],
     [7200, 0, 3600, 0.01, 0.5, 10, 15, 5],
     [7200, 0, 3600, 0.01, 0.5, 10, 5, 15],
     [7200, 0, 3600, 0.01, 0.5, 10, 15, 15]],
    [[7200, 0, 3600, 0.01, 0.5, 100, 9, 9],
     [7200, 0, 3600, 0.01, 0.5, 100, 11, 11]],
]


if __name__ == "__main__":
    result = simulation(configuration, log_enable=False)
    print(f"Result: {result}")