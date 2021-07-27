# Test case created based on test case used on LeetCode
import unittest
from anagram import Solution

class validAnagramTestCase(unittest.TestCase):
    
    def test_anagram(self):
        self.assertEqual(Solution().isAnagram("triangle","integral" ), 1, "Expected output is true")
        self.assertEqual(Solution().isAnagram("elbow","below"), 1, "Expected output is true")
        self.assertEqual(Solution().isAnagram("triangle", "boulder"), 0, "Expected output is false")
       
        
if __name__ == '__main__':
    unittest.main()