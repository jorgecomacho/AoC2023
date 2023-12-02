filename = 'day02.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def parse_lines(lines):
    bal = []
    for line in lines:
        mins = {'red':0, 'green':0, 'blue':0}
        game, moves = line.split(": ")
        move = moves.split("; ")
        for m in move:
            cubes = m.split(", ")
            for cube in cubes:
                tmpnum, tmpcol = cube.split(" ")
                if mins[tmpcol] < int(tmpnum):
                    mins[tmpcol] = int(tmpnum)
        bal.append(mins)
    return bal

def will_it_fit(bal):
    mins = {"red":12, "green":13, "blue":14}
    total = 0
    for i in range(len(bal)):
        test = True
        for color in mins.keys():
            print(bal[i][color], mins[color], color, i)
            if bal[i][color] > mins[color]:
                test= False
        if test:
            print('here')
            total += i+1
    return total

def powers(bal):
    total = 0
    for b in bal:
        tmp = 1
        for color in b.keys():
            tmp*=b[color]
        total+=tmp
    return total

if __name__ == "__main__":
    lines = read_file(filename)
    bal = parse_lines(lines)
    print(powers(bal))

    
    