class Solution(object):
    def longestCommonPrefix(self, strs):

        prefix = ""

        for i in range(len(strs[0])):
            for string in strs:
                if i>=len(string) or strs[0][i] != string[i]:
                    return prefix
            prefix += strs[0][i]

        return prefix

      










      