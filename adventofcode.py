def read_input():
    import urllib.request as urllib2
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'session=53616c7465645f5f95bf10e2fb5d361e577d9f15b2620b4bc260cf6af2c9fe4817022b374ccb115c9f7d82bd7a038f65'))
    response = opener.open("https://www.adventofcode.com/2021/day/3/input")
    content = response.readlines()
    input = []
    for line in content:
        input.append(str(line.decode("utf-8")).replace("\n", ""))
    return input

def day2_part1():
    moves = read_input()
    vertical, horizental = 0, 0
    for _ in moves:
        move = _.split(" ")
        if move[0] == "up":
            vertical -= int(move[1])
        if move[0] == "down":
            vertical += int(move[1])
        if move[0] == "forward":
            horizental += int(move[1])
    return vertical*horizental

def day2_part2():
    moves = read_input()
    depth, horizental, aim = 0, 0, 0
    for _ in moves:
        move = _.split(" ")
        if move[0] == "up":
            aim -= int(move[1])
        if move[0] == "down":
            aim += int(move[1])
        if move[0] == "forward":
            horizental += int(move[1])
            depth += int(move[1])*aim
    return depth*horizental

def day3_part1():
    # report = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    report = read_input()

    l = ["", "", "", "", ""]
    for line in report:
        for _ in range(0, 5):
            l[_] += line[_]
    gamma = ""
    epsilon = ""
    for _ in l:
        gamma += max(_, key=_.count)
        epsilon += min(_, key=_.count)
    return int(gamma, 2)* int(epsilon, 2)

def day3_part2():
    # report = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    report = read_input()
    min_report = [_ for _ in report]
    l = len(report[0])
    index = 0
    while index < l:
        if len(report)>1:
            m = {"1":0, "0":0}
            for _ in report:
                m[_[index]] += 1
            max_ = max(m, key=m.get)
            report = list(filter(lambda _: _[index] == max_, report))
        if len(min_report)>1:
            m2 = {"0":0, "1":0}
            for _ in min_report:
                m2[_[index]] += 1
            min_ = min(m2, key=m2.get)
            min_report = list(filter(lambda _: _[index] == min_, min_report))
        index += 1
    return int(report.pop(), 2)* int(min_report.pop(), 2)

if __name__=="__main__":
    print(day3_part2())