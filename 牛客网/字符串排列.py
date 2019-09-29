#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-28 上午10:09 
# @Author : Lattesea 
# @File : 字符串排列.py 
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""


class Solution:
    def Permutation(self, ss):
        if len(ss) <= 0:
            return []
        res = list()
        self.perm(ss, res, '')
        uniq = list(set(res))
        print(sorted(uniq))
        return sorted(uniq)

    def perm(self, ss, res, path):
        if ss == '':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i] + ss[i + 1:], res, path + ss[i])


if __name__ == '__main__':
    reuslt = Solution()
    reuslt.Permutation('123456')
