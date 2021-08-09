# Test case created based on test case used on LeetCode
import unittest
from duplicate import Solution

class duplicatesTestCase(unittest.TestCase):
    
    def test_uniqChar(self):
        self.assertEqual(Solution().containsDuplicate([1,2,3,1]), True, "Expected output is True")
        self.assertEqual(Solution().containsDuplicate([1,2,3,4]), False, "Expected output is False")
        self.assertEqual(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True, "Expected output is True")
        self.assertEqual(Solution().containsDuplicate([1,2,3,4,5,6,7,8,9]), False, "Expected output is False")
        
        
        
if __name__ == '__main__':
    unittest.main()
    
