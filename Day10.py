import copy
import re

def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

def calculateCentroid(positions):
    sumX = sumY = 0
    for i in range(0, len(positions)):
        sumX += positions[i][0]
        sumY += positions[i][1]
    return sumX / len(positions), sumY / len(positions)

# This is a faulty assumption, really want straightline distance from center
# of field of points to calculate area
def calculateDimensions(positions):
    maxX = minX = positions[0][0]
    maxY = minY = positions[0][1]
    for i in range(0, len(positions)):
        if positions[i][0] > maxX:
            maxX = positions[i][0]
        elif positions[i][0] < minX:
            minX = positions[i][0]
        if positions[i][1] > maxY:
            maxY = positions[i][1]
        elif positions[i][1] < minY:
            minY = positions[i][1]
    deltaX = maxX - minX
    deltaY = maxY - minY
    return deltaX, deltaY


def main():
    # Get values
    positions = []
    velocities = []
    with open("Inputs/Day10") as file:
        lines = file.readlines()
        for line in lines:
            p = re.compile("position=<\s*(-*\d+),\s+(-*\d+)>\svelocity=<\s*(-*\d+),\s+(-*\d+)>")
            m = p.match(line)
            positions.append((int(m.group(1)), int(m.group(2))))
            velocities.append((int(m.group(3)), int(m.group(4))))
            print m.group(1), m.group(2), m.group(3), m.group(4)
        dimensions = calculateDimensions(positions)
        minArea = dimensions[0] * dimensions[1]
        #positionsCopy = copy.copy(positions)
        seconds = 0
        print seconds, dimensions, area(positions)
        while 1:
            for i in range(0, len(positions)):
                positions[i] = (positions[i][0] + velocities[i][0],
                                positions[i][1] + velocities[i][1])
            dimensions = calculateDimensions(positions)
            tempArea = dimensions[0] * dimensions[1]
            if tempArea < minArea:
                minArea = tempArea
                #positionsCopy = copy.copy(positions)
            else:
                break
            seconds += 1
            print seconds, dimensions, area(positions)
        # dimensions = calculateDimensions(positionsCopy)
        # print seconds, dimensions[0] * dimensions[1]
        # for y in range(dimensions[4], dimensions[4]+dimensions[1]):
        #     for x in range(dimensions[2], dimensions[4]+dimensions[0]):
        #         for k in range(0, len(positionsCopy)):
        #             if x == positionsCopy[k][0] and y == positionsCopy[k][1]:
        #                 print "#",
        #             else:
        #                 print ".",
        #     print ""
