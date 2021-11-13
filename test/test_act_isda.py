import unittest
from yearfrac import act_isda


class Test_ActIsda(unittest.TestCase):

    def test1(self):
        x = act_isda(2018, 12, 15, 2019, 3, 1)
        # self.assertEquals(round(x, 15), 0.208219178082192)
        self.assertEquals(round(x, 8), round(0.208219178082118, 8))

    def test2(self):
        x = act_isda(2018, 12, 31, 2019, 1, 1)
        self.assertEquals(round(x, 8), round(1. / 365., 8))

    def test3(self):
        x = act_isda(1994, 6, 30, 1997, 6, 30)
        self.assertEquals(round(x, 8), 3.0)

    def test4(self):
        x = act_isda(1994, 2, 10, 1994, 6, 30)
        self.assertEquals(round(x, 8), round(140. / 365., 8))


# run
if __name__ == '__main__':
    unittest.main()
