#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""

Implement pow(x, n).


Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100

"""

__author__='lx'


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        s=x**n
        return s

solution=Solution()
s=solution.myPow(2.000,10)
print(s)