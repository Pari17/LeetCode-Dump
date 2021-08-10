# Test case created based on test case used on LeetCode
import unittest
from sqrt import Solution

class sqrtTestCase(unittest.TestCase):
    
    def test_sqrt(self):
        self.assertEqual(Solution().mySqrt(4), 2, "Expected output is 2")
        self.assertEqual(Solution().mySqrt(8), 2, "Expected output is 2")
        self.assertEqual(Solution().mySqrt(36), 6, "Expected output is 6")
       
        
        
        
if __name__ == '__main__':
    unittest.main()
    