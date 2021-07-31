# Test case created based on test case used on LeetCode
import unittest
from palindrome import Solution

class validPalindromeTestCase(unittest.TestCase):
    
    def test_anagram(self):
        self.assertEqual(Solution().isPalindrome("Sit on a potato pan, Otis" ), 1, "Expected output is true")
        self.assertEqual(Solution().isPalindrome("race an elephant"), 0, "Expected output is false")
       
        
if __name__ == '__main__':
    unittest.main()