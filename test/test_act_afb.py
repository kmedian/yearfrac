import unittest
from yearfrac import act_afb


class Test_ActAfb(unittest.TestCase):

    def test1(self):
        x = act_afb(2018, 12, 15, 2019, 3, 1)
        self.assertEquals(round(x, 8), 0.20547945)


# run
if __name__ == '__main__':
    unittest.main()
