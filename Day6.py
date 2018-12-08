def printGrid(grid):
    print "------------------------------"
    for i in range(0, len(grid)):
        print grid[i]
        #for j in range(0, len(grid[i])):
            #print grid[i][j]
        #print "\n"


def calculateManhattanDistance(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


def main():
    with open("Inputs/Day6") as file:
        lines = file.readlines()

        # Assemble coordinate list (key is coordinate tuple, value is value of area)
        coordinates = {}
        for line in lines:
            splitLines = line.split(",")
            coordinates[(int(splitLines[0]), int(splitLines[1]))] = 0

        # Figure out maximum dimensions
        maxX = maxY = 0
        for coordinate in coordinates.keys():
            if coordinate[0] > maxX:
                maxX = coordinate[0]
            if coordinate[1] > maxY:
                maxY = coordinate[1]
        maxX += 1
        maxY += 1
        print "Grid Dimensions:", maxX, maxY

        # TODO
        # possibly add in check for infinite (by plus oneing the dimensions)

        # Iterate through every point on the grid, calculating the Manhattan Distance to
        # each defined point, tallying each defined points area; also check for infinite area
        excludedCoordinates = []
        for x in range(0, maxX):
            for y in range(0, maxY):
                minManhattanDistance = calculateManhattanDistance((x, y), (coordinates.keys()[0]))
                minDistancePoints = []
                for coordinate in coordinates.keys():
                    md = calculateManhattanDistance((x, y), coordinate)
                    if md < minManhattanDistance:
                        minManhattanDistance = md
                        minDistancePoints = []
                        minDistancePoints.append(coordinate)
                    elif md == minManhattanDistance:
                        minDistancePoints.append(coordinate)
                if len(minDistancePoints) == 1:
                    coordinates[minDistancePoints[0]] += 1
                    if (x == 0 or x == maxX-1 or y == 0 or y == maxY-1) and minDistancePoints[0] not in excludedCoordinates:
                        excludedCoordinates.append(minDistancePoints[0])

        # Print out coordinates and counts
        for excludedCoordinate in excludedCoordinates:
            coordinates.pop(excludedCoordinate)
        for coordinate in coordinates.keys():
            print coordinate, coordinates[coordinate]


        #
        # # Fill out grid
        # grid = []
        # for i in range(0, maxX):
        #     column = []
        #     grid.append(column)
        #     for j in range(0, maxY):
        #         grid[i].append(".")
        # i = 65
        # for coordinate in coordinates:
        #     grid[coordinate[0]][coordinate[1]] = chr(i)
        #     i += 1
        #     printGrid(grid)
