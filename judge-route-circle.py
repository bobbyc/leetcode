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
        x = y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return ( x == 0 and y == 0)

if __name__ == '__main__':
    unittest.main()
