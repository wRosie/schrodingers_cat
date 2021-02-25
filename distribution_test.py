# Simple test for NeoPixels on Raspberry Pi
import time
import board
import random
import math
import statistics

rand_input = []


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def natural_infection():
    new_input = random.randint(0, 1280)
    rand_input.append(new_input)
    if len(rand_input) > 10 :
        rand_input.pop(0)
    map(sigmoid, rand_input)
    res = statistics.median(rand_input)
    return res


def one_trial():
    x = 0
    while True:
        res1 = natural_infection()
        threshold = random.randint(500000, 1000000)
        if res1 < threshold:
            print(x)
            return x
            #exit(0)
        x = x+1


for i in range(1000):
    print(natural_infection())

# arr_res = []
# for i in range(1000):
#     arr_res.append(one_trial())
# print(statistics.mean(arr_res))

# for i in range(1000) :
#     res1 = natural_infection()
#     arr_res.append(res1)
# print(statistics.mean(arr_res))
# arr_res = []
# for i in range(1000) :
#     res2 = natural_infection()
#     arr_res.append(res1)
# print(statistics.mean(arr_res))

