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
        nodeSums = []
        for i in range(0, numNodes):
            result = parseNode(data, current)
            current = result[0]
            nodeSums.append(result[1])
            #metaSum += result[1]
        for i in range(0, numMeta):
            index = int(data[current])-1
            if index < len(nodeSums) and index >= 0:
                metaSum += nodeSums[index]
            current += 1
    else:
        for i in range(0, numMeta):
            metaSum += int(data[current])
            current += 1

    return current, metaSum


def main():
    with open("Inputs/Day8") as file:
        line = file.readline()
        splitLine = line.split(" ")
        print parseNode(splitLine, 0)


