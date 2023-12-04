filename = 'day04.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

#part 1
def parse(lines):
    total = 0
    for line in lines:
        winners = line.strip().split(' | ')[0].split(': ')[1].split()
        numbers = line.strip().split(' | ')[1].split()
        #cast as sets and find union
        tmp = len(set(winners) & set(numbers))
        if tmp > 0:
            #waste 10 minutes remembering ^ vs **
            total += 2**(tmp-1)
    return total

#part 2
def funky_count(lines):
    #dictionary using lines index as key with running count as value
    card_counts = {i:1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        winners = line.strip().split(' | ')[0].split(': ')[1].split()
        numbers = line.strip().split(' | ')[1].split()
        tmp = len(set(winners) & set(numbers))
        #process each line x times based on its count
        for k in range(card_counts[i]):
            #add subsequent cards
            for j in range(tmp):
                card_counts[i+1+j] += 1
    return sum(card_counts.values())

if __name__ == "__main__":
    lines = read_file(filename)
    print(parse(lines))
    print(funky_count(lines))