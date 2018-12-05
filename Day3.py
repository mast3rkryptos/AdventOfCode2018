import re


def main():
    fabric = []
    for i in range(1000):
        column = []
        for j in range(1000):
            column.append(".")
        fabric.append(column)
    with open("Inputs/Day3") as file:
        lines = file.readlines()
        for line in lines:
            claim = xpos = ypos = xlen = ylen = 0
            p = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
            m = p.match(line)
            claim = int(m.group(1))
            xpos = int(m.group(2))
            ypos = int(m.group(3))
            xlen = int(m.group(4))
            ylen = int(m.group(5))

            for i in range(xpos, xpos+xlen):
                for j in range(ypos, ypos+ylen):
                    if fabric[i][j] is ".":
                        fabric[i][j] = str(claim)
                    else:
                        fabric[i][j] = "X"
        for line in lines:
            claim = xpos = ypos = xlen = ylen = 0
            p = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
            m = p.match(line)
            claim = int(m.group(1))
            xpos = int(m.group(2))
            ypos = int(m.group(3))
            xlen = int(m.group(4))
            ylen = int(m.group(5))

            check = True
            for i in range(xpos, xpos+xlen):
                for j in range(ypos, ypos+ylen):
                    check &= (fabric[i][j] is not "X")#str(claim))
            if check:
                print claim
    count = 0
    for column in fabric:
        for c in column:
            if c is "X":
                count += 1
    print count
