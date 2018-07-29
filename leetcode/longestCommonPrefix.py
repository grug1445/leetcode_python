#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_len = len(strs)
        if str_len == 0:
            return ""
        if str_len == 1:
            return strs[0]
        first = strs[0]
        array = list(first)
        array_len = len(array)
        if array_len == 0:
            return ""
        tmp = array[0]
        for index in range(array_len):
            if index != 0:
                tmp += array[index]
            for str_index in range(1, str_len):
                str_now = strs[str_index]
                if len(str_now) < len(tmp):
                    return tmp[0:index]
                if tmp == strs[str_index][0:index + 1]:
                    continue
                else:
                    if index == 0:
                        return ""
                    elif index > 0:
                        return tmp[0:index]
                    else:
                        return ""

        return tmp


if __name__ == "__main__":
    solution = Solution()
    param_list = ["cisk", "csj", "ckk"]
    print solution.longestCommonPrefix(param_list)
