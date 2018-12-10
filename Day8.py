# Recursive
# Returns a tuple: (size of node, sum of metadaata)
def parseNode(data, root):
    # Get the number of subnodes
    current = root
    numNodes = int(data[current])
    # Get the number of metadata entries
    current += 1
    numMeta = int(data[current])
    # Process subnodes and get metadata
    current += 1
    metaSum = 0
    if numNodes != 0:
        for i in range(0, numNodes):
            result = parseNode(data, current)
            current = result[0]
            metaSum += result[1]
    for i in range(0, numMeta):
        metaSum += int(data[current])
        current += 1

    return current, metaSum


def main():
    with open("Inputs/Day8") as file:
        line = file.readline()
        splitLine = line.split(" ")
        print parseNode(splitLine, 0)


