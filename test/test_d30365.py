import unittest
from yearfrac import d30365


class Test_ActIsda(unittest.TestCase):

    def test1(self):
        x = d30365(2018, 12, 15, 2019, 3, 1)
        self.assertEquals(round(x, 8), 0.20821918)


# run
if __name__ == '__main__':
    unittest.main()
