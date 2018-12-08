import re

NUMBER_OF_WORKERS = 5
BASE_TIME = 60

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

        order = ""
        workers = {}
        second = -1
        for i in range(0, NUMBER_OF_WORKERS):
            workers[i] = (["", 0])
        done = False
        while not done:
            second += 1
            for worker in workers.keys():
                if workers[worker][1] > 0:
                    workers[worker][1] -= 1
                else:
                    for step in sorted(steps.keys()):
                        if workers[worker][0] in steps[step]:
                            steps[step].remove(workers[worker][0])
                    if workers[worker][0] not in order:
                        order += workers[worker][0]
                        workers[worker] = ("", 0)
                        if len(steps) == 0:
                            done = True
                            for i in range(0, NUMBER_OF_WORKERS):
                                done &= workers[i] == ("", 0)
                    for step in sorted(steps.keys()):
                        if len(steps[step]) == 0:
                            workers[worker] = [step, BASE_TIME + (ord(step) - 64) - 1]
                            del steps[step]
                            break

        print order, second

