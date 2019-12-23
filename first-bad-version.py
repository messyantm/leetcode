"""
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。 
"""
import bisect


class A:
    def __init__(self):
        self.__class__.__getitem__ = lambda self, x: isBadVersion(x)


def init_bade_version(bad_version):
    def isBadVersion(version):
        if version >= bad_version:
            return True
        else:
            return False

    return isBadVersion


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        tail = n
        while True:
            m = (head + tail) // 2
            if isBadVersion(m):
                if isBadVersion(m - 1) is False:
                    return m
                else:
                    tail = m - 1
            else:
                head = m + 1


class Solution2:
    def firstBadVersion(self, n):
        self.__class__.__getitem__ = lambda self, x: isBadVersion(x)
        return bisect.bisect_left(self, True, 1, n)


if __name__ == "__main__":
    isBadVersion = init_bade_version(3)
    print(Solution().firstBadVersion(5))
