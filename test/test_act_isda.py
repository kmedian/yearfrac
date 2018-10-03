import unittest
from yearfrac import act_isda


class Test_ActIsda(unittest.TestCase):

    def test1(self):
        x = act_isda(2018, 12, 15, 2019, 3, 1)
        self.assertEquals(round(x, 8), 0.20547945)


# run
if __name__ == '__main__':
    unittest.main()
