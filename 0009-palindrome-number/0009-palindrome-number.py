class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev=0
        original_num=x
        while x>0:
            m=x%10
            rev=rev*10+m
            x=x/10
        return original_num==rev
            