# Recursive
# Returns a tuple: (size of node, sum of metadaata)
def parseNode(data, root):
    numNodes = data[root]
    numMeta = data[root+1]
    metaSum = 0
    nodeSize = 2 + numMeta
    if numNodes == 0:
        for i in range(0, numMeta):
            metaSum += data[root+2+i]
    else:
        offset = 2
        for i in range(0, numNodes):
            parseNode(data, root + offset)

    return (nodeSize, metaSum)

def main():
    with open("Inputs/Day8") as file:
        line = file.readline()
        splitLine = line.split(" ")
        print parseNode(splitLine, 0)


