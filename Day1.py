def main():
    duplicateFound = False
    frequencyList = [0]
    initialValue = 0
    with open("Inputs/Day1") as file:
        lines = file.readlines()
        while not duplicateFound:
            print "Still Looking"
            for line in lines:
                initialValue += int(line)
                if initialValue not in frequencyList:
                    frequencyList.append(initialValue)
                else:
                    duplicateFound = True
                    break
    print initialValue
