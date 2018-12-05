def compare(input1, input2):
    retVal = 0
    for i in range(len(input1)-1):
        if input1[i] != input2[i]:
            retVal += 1
    return retVal


def main():
    with open("Inputs/Day2") as file:
        lines = file.readlines()
        for line1 in lines:
            for line2 in lines:
                if compare(line1, line2) == 1:
                    print line1 + "\n" + line2
