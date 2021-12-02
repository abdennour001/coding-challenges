def add(c, k):
    c.test = c.test + 1
    k = k + 1

class Plus:
    def __init__(self):
        self.test = 0

def main():
    p = Plus()
    index = 0

    for i in range(25):
        add(p, index)

    print("test=", p.test)
    print("index", index)

main()