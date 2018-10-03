import unittest
from yearfrac import eastersunday


class Test_EasterSunday(unittest.TestCase):

    def test1(self):
        y = 2019
        m, d = eastersunday(y)
        self.assertEquals(m, 4)
        self.assertEquals(d, 21)


if __name__ == '__main__':
    unittest.main()
