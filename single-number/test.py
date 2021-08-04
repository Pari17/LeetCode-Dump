# Test case created based on test case used on LeetCode
import unittest
from single_number import Solution

class singleNumberTestCase(unittest.TestCase):
    
    def test_uniqChar(self):
        self.assertEqual(Solution().singleNumber([2,2,1]), 1, "Expected number is 1")
        self.assertEqual(Solution().singleNumber([4,1,2,1,2]), 4, "Expected number is 4")
        self.assertEqual(Solution().singleNumber([1]), 1, "Expected number is 1")
        self.assertEqual(Solution().singleNumber([-89,4,4,3,3,6,6]), -89, "Expected number is -89")  
        
if __name__ == '__main__':
    unittest.main()
