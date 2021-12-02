import math
import itertools


class Solution(object):

    def recursiveSolution(self, n, endDay):
        # base case 1
        if n == len(self.courses)-1:
            if self.courses[n][0] + endDay <= self.courses[n][1]:
                return 1
            else:
                return 0

        # duration + endDay <= deadline
        # 10 + 30th ... 50th | 10 + 30th ... 20th
        if self.courses[n][0] + endDay <= self.courses[n][1]:
            # either i take the course or not (the max between them)
            return max(self.recursiveSolution(n+1, endDay), self.recursiveSolution(n+1, endDay+self.courses[n][0])+1)
        else:
            # i must move forward
            return self.recursiveSolution(n+1, endDay)
    
    def heapSolution(self):
        pass

    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        self.courses = courses
        self.courses.sort(key=lambda course: (course[1], course[0]))
        maxDay = self.courses[len(self.courses)-1][1]
        # result = [sum(seq) for i in range(len(self.courses), 0, -1) for seq in itertools.combinations([c[0] for c in self.courses], i) if sum(seq) <= maxDay]

        # M = {(n, endDay):3} ex. {(3, 400):2}
        self.M = {}
        return self.heapSolution()


if __name__ == "__main__":
    # 5
    s = Solution()
    print(s.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
                           ))
