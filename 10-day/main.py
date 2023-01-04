import numpy as np
import pandas as pd

#  file = 'sample.txt'
file = 'input.txt'

instructions = open(file).readlines()

#  instructions = ['noop', 'addx 3', 'addx -5']

class Ticker:
    def __init__(self):
        self.counter = 0
        self.X = 1
        self.history = []

    def tick(self):
        self.counter += 1

    def check(self):
        if self.counter % 40 == 20:
            self.history.append((self.counter, self.X))

    def proc(self, instr):
        self.tick()
        self.check()
        if instr[:4] == 'addx':
            V = int(instr.split()[1])
            self.tick()
            self.check()
            self.X += V

    def calc_strength(self):
        return sum([a*b for a, b in self.history])

ticker = Ticker()
for instruction in instructions:
    ticker.proc(instruction)

print(f"A ::: {ticker.calc_strength()}")

class TickerB:
    def __init__(self):
        self.counter = 0
        self.X = 1
        self.drawings = []

    def tick(self):
        self.counter += 1

    def draw(self):
        pos = (self.counter - 1) % 40
        if abs(pos - self.X) <= 1:
            char = '#'
        else:
            char = '.'
        self.drawings.append((pos, char))

    def proc(self, instr):
        self.tick()
        self.draw()
        if instr[:4] == 'addx':
            V = int(instr.split()[1])
            self.tick()
            self.draw()
            self.X += V

    def print(self):
        for i, char in self.drawings:
            if i % 40 == 0:
                print()
            print(char, end='')
        print()
        print()

ticker = TickerB()
for instruction in instructions:
    ticker.proc(instruction)

ticker.print()


