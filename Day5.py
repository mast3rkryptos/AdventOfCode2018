def react(input):
    # -1 length to prevent overrun
    for i in range(0, len(input)-1):
        if ord(input[i]) == (ord(input[i+1]) + 32) or ord(input[i]) == (ord(input[i+1]) - 32):
            del input[i]
            del input[i]
            return 1
    return 0



def main():
    with open("Inputs/Day5") as file:
        unitTypes = {}
        line = file.readline()
        for i in range(65, 65+26):
            chars = []
            lineCopy = line
            lineCopy = lineCopy.replace(chr(i), "")
            lineCopy = lineCopy.replace(chr(i+32), "")
            for c in lineCopy:
                chars.append(c)
            count = 1
            while react(chars) != 0:
                #print "Reaction #", count
                count += 1
            print "Result", chr(i), len(chars)
            unitTypes[chr(i)] = len(chars)
        minCount = unitTypes["A"]
        unitTypePick = "A"
        for unitType in unitTypes.keys():
            if unitTypes[unitType] < minCount:
                unitTypePick = unitType
                minCount = unitTypes[unitType]
        print "Answer", unitTypePick, minCount
