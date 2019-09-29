#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午2:17 
# @Author : Lattesea 
# @File : 测试.py 
import collections


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        flag = False
        c = collections.Counter(numbers)
        for k, v in c.items():
            if v > 1:
                duplication[0] = k
                flag = True
                break
        return flag


if __name__ == '__main__':
    result = Solution()
    s = {2, 3, 1, 0, 2, 5, 3}
    result.duplicate(7, s)
