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
        line = file.readline()
        chars = []
        for c in line:
            chars.append(c)
        count = 1
        while react(chars) != 0:
            #print "Reaction #", count
            count += 1
        print "Result", len(chars)
