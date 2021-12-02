def read_input():
    import urllib.request as urllib2
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'session=53616c7465645f5f95bf10e2fb5d361e577d9f15b2620b4bc260cf6af2c9fe4817022b374ccb115c9f7d82bd7a038f65'))
    response = opener.open("https://www.adventofcode.com/2021/day/2/input")
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

if __name__=="__main__":
    print(day2_part2())