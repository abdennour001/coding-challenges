import sys


class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize+1)
        self.heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = (self.heap[spos], self.heap[fpos])

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.heap[pos] < self.heap[self.leftChild(pos)]) or (self.heap[pos] < self.heap[self.rightChild(pos)]):
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):
        pass

    def print(self):
        pass

    def extractMax(self):
        pass


if __name__ == "__main__":

    max_heap = MaxHeap(15)
