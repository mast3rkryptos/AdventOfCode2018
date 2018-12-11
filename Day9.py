class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = self
        self.prev = self

    def append(self, val):
        dn = DoublyNode(val)
        self.next.prev = dn
        dn.next = self.next
        dn.prev = self
        self.next = dn
        return dn

    def insert(self, val):
        dn = DoublyNode(val)
        self.prev.next = dn
        dn.prev = self.prev
        dn.next = self
        self.prev = dn

    def pop(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.val


class MarbleCircle:
    def __init__(self):
        self.current = DoublyNode(0)

    def placeMarble(self, value):
        score = 0
        if value % 23 == 0:
            temp = self.current.prev.prev.prev.prev.prev.prev
            self.current = temp.prev
            score += value + self.current.pop()
            self.current = temp
        else:
            self.current = self.current.next.append(value)
        return score

def main():
    playerCount = 0
    maxMarbleValue = 0
    # Get values
    with open("Inputs/Day9") as file:
        # Get values
        lines = file.readlines()
        for line in lines:
            splitLine = line.split(" ")
            playerCount = int(splitLine[0])
            maxMarbleValue = int(splitLine[6])
            # Set up scoreboard
            playerScores = []
            for i in range(0, playerCount):
                playerScores.append(0)
            # Begin placing marbles
            currentPlayer = 0
            mc = MarbleCircle()
            for i in range(1, maxMarbleValue+1):
                if i % 10000 == 0:
                    print i
                playerScores[currentPlayer] += mc.placeMarble(i)
                currentPlayer = (currentPlayer + 1) % playerCount
            # Find max score
            maxScore = 0
            for i in range(0, len(playerScores)):
                if playerScores[i] > maxScore:
                    maxScore = playerScores[i]
            print maxScore


