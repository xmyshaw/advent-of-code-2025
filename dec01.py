import math

def part1(input_str):
    count_zero = 0
    pos = 50 # start position
    for line in input_str.split('\n'):
        direction = line[0]
        steps = int(line[1:])
        if direction == "R":
            pos = (pos + steps) % 100
        if direction == "L":
            pos = (pos - steps) % 100
            if pos < 0:
                pos = 100 + pos
        if pos == 0:
            count_zero +=1
    print(f'Total number of 0 is: {count_zero}')

