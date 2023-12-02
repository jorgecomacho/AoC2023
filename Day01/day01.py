filename = 'day01.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def replace_line(lines):
    spelled = {'one':'1','two':'2','three':'3','four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    mod_lines = []
    total = 0

    for line in lines:
        index = 0
        start = 0
        first = False
        last = False
        for i in range(len(line)):
            if first:
                break
            if line[i].isdigit():
                start = int(line[i])
                first = True
                continue
            for num in spelled.keys():
                if line[i:].startswith(num) and not first:
                    start = int(spelled[num])
                    first = True
                    break

        end = 0
        for i in range(len(line)-1, -1, -1):
            if last:
                break
            if line[i].isdigit():
                end = int(line[i])
                last = True
                continue
            for num in spelled.keys():
                if line[0:i+1].endswith(num):
                    end = int(spelled[num])
                    last = True
                    break
        print(line, start, end)
        total += start*10 + end
        print(total)
        
    return total

def clear_lines(lines):
    total=0
    for line in lines:
        tmp = ''
        for c in line:
            if c.isdigit():
                tmp+=c
        tmp = tmp[0]+tmp[-1]
        total+=int(tmp)
    return total

if __name__ == "__main__":
    lines = read_file(filename)
    mod = replace_line(lines)
    print(mod)

    
    