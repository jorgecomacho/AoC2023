filename = 'day03.txt'
#filename = 'test.txt'

import os, re

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

#part 1
def parse_this_bs(lines):
    total = 0
    # all symbols used
    symbols = ['*', '%', '-', '#', '=', '@', '$', '/', '+', '&']
    for i in range(len(lines)):
        tmp = ''
        for j in range(len(lines[i])):
            #finds a digit, skips the rest of the loop until number is complete or line end
            if lines[i][j].isdigit():
                tmp += lines[i][j]
                if j < len(lines[i]) -1 and lines[i][j+1].isdigit():
                    continue
            #only gets here after assembling a number
            if len(tmp) > 0:
                adjacent = False
                for k in range(i-1,i+2,1):
                    if adjacent:
                        break
                    for l in range(j-len(tmp),j+2, 1):
                        #try block to lazily avoid enforcing boundaries
                        try:
                            if lines[k][l] in symbols:
                                adjacent = True
                                break
                        except:
                            pass
                if adjacent:
                    #adds to total if adjacent to any symbol
                    total += int(tmp)
                tmp = ''
    return total

#part 2 before i rage quit for a while and built a better one, but it works
def this_blows(lines):
    total = 0
    #idea was to build a list of stars with their location, count of adjacent numbers and a running product
    stars = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '*':
                #temp dict object to be added to stars
                tmp={}
                tmp['row'] = i
                tmp['col'] = j
                tmp['count'] = 0
                tmp['product'] = 1
                stars.append(tmp)
    #ideally should have a list of star dicts, now just iterating through to find digits like part 1
    for i in range(len(lines)):
        tmp = ''
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                tmp += lines[i][j]
                if j < len(lines[i]) -1 and lines[i][j+1].isdigit():
                    continue
            #was building number, but finished
            if len(tmp) > 0:
                for k in range(i-1,i+2,1):
                    for l in range(j-len(tmp),j+2, 1):
                        for star in stars:
                            # idea was to see when an adjacent node to a number matched a star coord
                            # then increment adjacency count and update running product
                            if star['row'] == k and star['col'] == l:
                                star['count'] += 1
                                star['product'] *= int(tmp)
                # reset to empty tmp value to allow multiple nums on same line
                tmp = ''
    for star in stars:
        if star['count'] == 2:
            total += star['product']
    return total

# part 2 proper-ish solution using regex and crap
def oof(lines):
    #dict using coordinates as key, with list of numbers as value
    stars = {}
    total = 0
    for i in range(len(lines)):
        # regex per line to match numbers
        for num in re.finditer(r"\d+", lines[i]):
            # build list of coordinates for adjacent spaces, enforce boundaries
            adjacent = [(i-1, j) for j in range(num.start()-1, num.end()+1, 1) if -1<j<len(lines[i]) and i>1]
            if -1 < num.start() -1:
                adjacent.append((i, num.start()-1))
            if num.end() < len(lines[i]):
                adjacent.append((i, num.end()))
            adjacent += [(i+1, j) for j in range(num.start()-1, num.end()+1, 1) if -1<j<len(lines[i]) and i+1<len(lines[i])]
            # check all adjacent coords for stars
            for row, col in adjacent:
                if lines[row][col] == '*':
                    # lazy try block to avoid index not existing errors, should probably have done
                    # differently
                    try:
                        stars[row, col].append(num.group())
                    except:
                        stars[row, col] = [num.group()]
    # update total
    for a, b in stars.keys():
        if len(stars[a,b]) == 2:
            total += int(stars[a,b][0]) * int(stars[a,b][1])
    return total

if __name__ == "__main__":
    lines = read_file(filename)
    print(parse_this_bs(lines))
    print(this_blows(lines))
    print(oof(lines))