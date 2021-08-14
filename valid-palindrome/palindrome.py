import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """   
        str1 = re.sub(r'[\W_]+', '', s).lower()
        str2 = str1[::-1].lower()

        if str1 == str2:
            print("True")
            return 1
        print("False")
        return 0
