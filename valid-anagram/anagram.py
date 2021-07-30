class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            print("False")
            return 0
       
        s = sorted(s)
        t = sorted(t)
        
        for i in range(0, len(s)):
            if s[i] != t[i]:
                print("False")
                return 0

        print("True")
        return 1
    
    '''
    Alternatively, version 2 of the code above is as follows:
    
    if sorted(s) == sorted(t):
            return(1)
        return(0)
        
   '''
