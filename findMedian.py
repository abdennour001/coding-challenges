import heapq


class MedianFinder:
    def __init__(self):
        self.minstream = []
        self.maxstream = []

    def addNum(self, num: int) -> None:
        # if len(self.maxstream) == 0 and len(self.minstream) > 0:
        #     if num <= self.minstream[0]:
        #         heapq.heappush(self.maxstream, -num)
        #     else:
        #         heapq.heappush(self.minstream, -heapq.heappop(self.maxstream))
        #         heapq.heappush(self.maxstream, -num)
        #     print(self.maxstream)
        #     print(self.minstream)
        #     return
        if len(self.minstream) == 0 and len(self.maxstream) > 0:
            if num >= -self.maxstream[0]:
                heapq.heappush(self.minstream, num)
            else:
                heapq.heappush(self.minstream, -heapq.heappop(self.maxstream))
                heapq.heappush(self.maxstream, -num)
            print(self.maxstream)
            print(self.minstream)
            return
        elif len(self.maxstream) == 0 and len(self.minstream) == 0:
            heapq.heappush(self.maxstream, -num)
            print(self.maxstream)
            print(self.minstream)
            return

        if len(self.maxstream) == len(self.minstream):
            if num <= self.minstream[0]:
                heapq.heappush(self.maxstream, -num)
            else:
                heapq.heappush(self.maxstream, -heapq.heappop(self.minstream))
                heapq.heappush(self.minstream, num)
        elif len(self.maxstream) > len(self.minstream):
            if num >= -self.maxstream[0]:
                heapq.heappush(self.minstream, num)
            else:
                heapq.heappush(self.minstream, -heapq.heappop(self.maxstream))
                heapq.heappush(self.maxstream, -num)
        # elif len(self.maxstream) < len(self.minstream):
        #     if num <= self.minstream[0]:
        #         heapq.heappush(self.maxstream, -num)
        #     else:
        #         heapq.heappush(self.minstream, -heapq.heappop(self.maxstream))
        #         heapq.heappush(self.maxstream, -num)
        print(self.maxstream)
        print(self.minstream)

    def findMedian(self) -> float:
        if len(self.maxstream) > len(self.minstream):
            return -self.maxstream[0]
        elif len(self.maxstream) < len(self.minstream):
            return self.minstream[0]
        else:
            return (-self.maxstream[0] + self.minstream[0]) / 2


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(4)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(7)
    print(obj.findMedian())
    obj.addNum(8)
    print(obj.findMedian())