# Test case created based on test case used on LeetCode
import unittest
from roman import Solution

class romanTestCase(unittest.TestCase):
    
    def test_roman(self):
        self.assertEqual(Solution().romanToInt("IV"), 4, "Expected index number is 4")
        self.assertEqual(Solution().romanToInt("IX"), 9, "Expected index number is 9")
        self.assertEqual(Solution().romanToInt("LVIII"), 58, "Expected index number is 58")
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 58, "Expected index number is 58")
 
        
if __name__ == '__main__':
    unittest.main()
    
