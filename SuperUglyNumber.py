from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # seq = []
        # for _ in range(1, 10000):
        #     factors = []
        #     for i in range(2, _ + 1):
        #         if _ % i == 0:
        #             count = 1
        #             for j in range(2, (i//2 + 1)):
        #                 if(i % j == 0):
        #                     count = 0
        #                     break
        #             if(count == 1):
        #                 factors.append(i)
        #     flag=True
        #     for p in factors:
        #         if p not in primes:
        #             flag=False
        #             break
        #     if flag==True:
        #         seq.append(_)
        #     if len(seq) == n:
        #         return seq.pop()
        h = []
        ans = [1]
        for _ in primes:
            if ans[-1]*_ not in h:
                heapq.heappush(h, ans[-1]*_)
        s = ans[-1]*primes[0]
        p = heapq.heappop(h)
        while len(ans) <= n:
            print(p, s)
            while p < s:
                ans.append(p)
                if len(ans) >= n:
                    break
                for _ in primes:
                    if p*_ not in h:
                        heapq.heappush(h, p*_)
                p = heapq.heappop(h)
            ans.append(p)
            if len(ans) >= n:
                break
            for _ in primes:
                if p*_ not in h:
                    heapq.heappush(h, p*_)
            p = heapq.heappop(h)
            s = p*primes[0] 
            print(ans)
            print(h)

        return ans[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))
