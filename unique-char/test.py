# Test case created based on test case used on LeetCode
import unittest
from first_unique_char import Solution

class uniqCharTestCase(unittest.TestCase):
    
    def test_uniqChar(self):
        self.assertEqual(Solution().firstUniqChar("Hello"), 0, "Expected index number is 0")
        self.assertEqual(Solution().firstUniqChar("loveletter"), 1, "Expected index number is 1")
        self.assertEqual(Solution().firstUniqChar("llama"), 3, "Expected index number is 3")
        self.assertEqual(Solution().firstUniqChar("xxyy"), -1, "Expected index number is -1")   
        
if __name__ == '__main__':
    unittest.main()
    
