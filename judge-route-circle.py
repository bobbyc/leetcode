import unittest

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test1(self):
        self.assertTrue(self.s.judgeCircle('UD'))

    def test2(self):
        self.assertFalse(self.s.judgeCircle('UDRLRLRLU'))

    def test3(self):
        self.assertFalse(self.s.judgeCircle('UDABR'))

# Definition for singly-linked list.
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

if __name__ == '__main__':
    unittest.main()
