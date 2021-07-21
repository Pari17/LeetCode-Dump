from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """          
        frequency = Counter(s)
        for i, char in enumerate (s):
            if frequency[char] == 1:
                print("Index of the non-repeating charater of the input string is:",i)
                return i     
        return -1
     
            
