# import matplotlib.pyplot as plt
import random
import math
### Parameters

#simulation size
NUM_PPL = 100000
NUM_DAYS = 365

#infection-related rates
MEETING_RATE_HEALTHY = 12
MEETING_RATE_SICK = 2
DAY_OF_SICKNESS = 6
INFECTION_RATES = [0, 0.00625, 0.0125, 0.025, 0.05, 0.1, 0.2, 0.15, 0.125, 0.1, 0.05, 0.025, 0.0125, 0.00625]
INFECTION_RATES = list(map(lambda x: x / 1.2, INFECTION_RATES))
IMMUNITY_RATE = 0.95

def run_simulation():
    num_susceptible = NUM_PPL - 1
    num_infected = 1
    num_recovered = 0


    days_left_infected_list = [14]
    daily_infections = []
    num_zeros = 0
    infections = 0
    f = open("out.csv", "w")
    for day in range(NUM_DAYS):
        days_left_infected_list = days_left_infected_list[num_zeros:]
        num_zeros = 0
        normal_meetings = int(math.floor(min(12, 6 * NUM_PPL / (1000 * infections + 1))))
        infections = 0
        if (day > 180 and day < 235):
            for i in range(len(INFECTION_RATES)):
                INFECTION_RATES[i] *= 1.015
        for i in range(len(days_left_infected_list)):
            daysleft = days_left_infected_list[i]
            infection_rate = INFECTION_RATES[14 - daysleft]
            daysleft -= 1
            days_left_infected_list[i] -= 1
            sick = daysleft < 9
            if sick:
                if (random.random() < 0.5):
                    num_meetings = 2
                else:
                    num_meetings = 1
            else:
                num_meetings = int(normal_meetings)
            for meeting in range(num_meetings):
                rand = random.random()
                if rand < infection_rate * num_susceptible / NUM_PPL:
                    infections += 1
                    num_infected += 1
                    num_susceptible -= 1
            if not daysleft:
                num_zeros += 1
                num_infected -= 1
                rand2 = random.random()
                if rand2 < IMMUNITY_RATE:
                    num_recovered += 1
                else:
                    num_susceptible += 1
        daily_infections.append(infections)
        for i in range(infections):
            days_left_infected_list.append(14)

    print(daily_infections)
    print(num_susceptible / NUM_PPL)
    f.write(str(daily_infections)[1:-1])
    print(1.015 ** 55)

run_simulation()