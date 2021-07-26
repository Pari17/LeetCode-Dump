# Test case created based on test case (custom judge) used on LeetCode
import unittest
from remove_duplicates import Solution

class removeDuplicatesTestCase(unittest.TestCase):
    
    def test_duplicates(self):
        a = [1,1,2]
        self.assertEqual(Solution().removeDuplicates(a), 2, "Expected length is 2")
       
       
        
if __name__ == '__main__':
    unittest.main()
    
