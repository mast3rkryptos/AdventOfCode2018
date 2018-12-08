import re

NUMBER_OF_WORKERS = 2
BASE_TIME = 0

def main():
    with open("Inputs/Day7") as file:
        steps = {}
        lines = file.readlines()
        p = re.compile("Step ([A-Z]).*step ([A-Z])")
        for line in lines:
            m = p.match(line)
            if m.group(1) not in steps.keys():
                steps[m.group(1)] = []
            if m.group(2) not in steps.keys():
                steps[m.group(2)] = []
            steps[m.group(2)].append(m.group(1))
        current = None
        for step in sorted(steps.keys()):
            if len(steps[step]) == 0:
                current = step
                break
        print current

        order = current
        workers = []
        for i in range(0, NUMBER_OF_WORKERS):
            workers[i] = 0
        while len(steps) > 0:
            for step in sorted(steps.keys()):
                if current in steps[step]:
                    steps[step].remove(current)
            del steps[current]
            for step in sorted(steps.keys()):
                if len(steps[step]) == 0:
                    current = step
                    order += current
                    break
        print order

