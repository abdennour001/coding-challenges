import math


class Solution(object):

    # def sigmoid(self, x):
    #     return 1 / (1+math.exp(-x))

    # def abd_func(self, diff, maxDay, endDay):
    #     if maxDay == endDay:
    #         return self.sigmoid((diff*maxDay) / endDay**2)
    #     return self.sigmoid((diff*(maxDay - endDay)) / endDay**2)

    # def scheduleCourse(self, courses):
    #     """
    #     :type courses: List[List[int]]
    #     :rtype: int
    #     """
    #     courses = list(filter(lambda x: x[0] <= x[1], courses))
    #     courses.sort(key=lambda course: (course[1], course[0]))
    #     if len(courses) == 0:
    #         return 0
    #     maxDay = courses[len(courses)-1][1]
    #     fun_map = {}
    #     for course in courses:
    #         fun_map[tuple(course)] = self.abd_func(
    #             course[1] - course[0], maxDay, course[1])
    #     # print(fun_map)
    #     fun_map = dict(
    #         sorted(fun_map.items(), key=lambda item: item[1], reverse=True))
    #     i = 0
    #     sum_days = 0
    #     while sum_days <= maxDay and i < len(list(fun_map.keys())):
    #         sum_days += list(fun_map.keys())[i][0]
    #         i += 1
    #     if sum_days > maxDay:
    #         i -= 1
    #     print(fun_map)
    #     return i

    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        pass


if __name__ == "__main__":
    # 5
    s = Solution()
    # print(s.scheduleCourse([[5, 15], [3, 19], [6, 7], [
    #       2, 10], [5, 16], [8, 14], [10, 11], [2, 19]]))
    print(s.scheduleCourse(
        [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
    # print(s.scheduleCourse(
    #     [[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]]
    # ))
