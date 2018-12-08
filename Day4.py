import re


def main():
    guards = {}
    guard = start = -1
    with open("Inputs/Day4") as file:
        lines = file.readlines()
        lines.sort()
        p = re.compile("\[\d\d\d\d\-\d\d\-\d\d \d\d:(\d\d)\] (?:(?:Guard \#(\d+))|(\w+))")

        # Find guard asleep the most
        for line in lines:
            m = p.match(line)
            # Guard begins shift
            if m.group(3) is None:
                guard = int(m.group(2))
                if guard not in guards.keys():
                    guards[guard] = 0
            # Guard falls asleep
            elif m.group(3) == "falls":
                start = int(m.group(1))
            # Guard wakes up
            elif m.group(3) == "wakes":
                elapsed = int(m.group(1)) - start
                guards[guard] += elapsed
        maxTime = 0
        guardPick = -1
        for guard in guards.keys():
            if guards[guard] > maxTime:
                guardPick = guard
                maxTime = guards[guard]

        # Find the minute picked guard was asleep the most often
        minutes = {}
        guardActive = False
        for i in range(0, 60):
            minutes[i] = 0
        for line in lines:
            m = p.match(line)
            # Guard begins shift
            if m.group(2) == str(guardPick):
                guardActive = True
            # Guard falls asleep
            elif guardActive and m.group(3) == "falls":
                start = int(m.group(1))
            # Guard wakes up
            elif guardActive and m.group(3) == "wakes":
                for i in range(start, int(m.group(1))):
                    minutes[i] += 1
            else:
                guardActive = False
        maxCount = 0
        minutePick = -1
        for minute in minutes.keys():
            if minutes[minute] > maxCount:
                minutePick = minute
                maxCount = minutes[minute]
        print "Strategy 1:", guardPick, minutePick, (guardPick * minutePick)

        # Find the most consistently asleep guard
        guards2 = {}
        for guardPick in guards.keys():
            minutes = {}
            guardActive = False
            for i in range(0, 60):
                minutes[i] = 0
            for line in lines:
                m = p.match(line)
                # Guard begins shift
                if m.group(2) == str(guardPick):
                    guardActive = True
                # Guard falls asleep
                elif guardActive and m.group(3) == "falls":
                    start = int(m.group(1))
                # Guard wakes up
                elif guardActive and m.group(3) == "wakes":
                    for i in range(start, int(m.group(1))):
                        minutes[i] += 1
                else:
                    guardActive = False
            maxCount = 0
            minutePick = -1
            for minute in minutes.keys():
                if minutes[minute] > maxCount:
                    minutePick = minute
                    maxCount = minutes[minute]
            guards2[guardPick] = (minutePick, maxCount)
            print "Strategy pre-2:", guardPick, minutePick, maxCount, (guardPick * minutePick)
        maxCount = 0
        guardPick = -1
        for guard in guards2.keys():
            if guards2[guard][1] > maxCount:
                guardPick = guard
                maxCount = guards2[guard][1]
        print "Strategy 2:", guardPick, guards2[guardPick][0], guards2[guardPick][1], (guardPick * guards2[guardPick][0])
