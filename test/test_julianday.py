import unittest
from yearfrac import date_to_jd, jd_to_date


class Test_JulianDay(unittest.TestCase):
    def test1(self):
        # 24-Nov (-4713) 12Uhr
        y, m, d = jd_to_date(0)
        # print("\nDate: {0:04d}-{1:02d}-{2:02d}".format(y, m, d))
        self.assertEquals(y, -4713)
        self.assertEquals(m, 11)
        self.assertEquals(d, 24)

    def test2(self):
        # 25-Nov (-4713) 12Uhr
        y, m, d = jd_to_date(1)
        # print("\nDate: {0:04d}-{1:02d}-{2:02d}".format(y, m, d))
        self.assertEquals(y, -4713)
        self.assertEquals(m, 11)
        self.assertEquals(d, 25)

    def test3(self):
        # 11-Feb-2014 12Uhr, 2456700
        y, m, d = jd_to_date(2456700)
        # print("\nDate: {0:04d}-{1:02d}-{2:02d}".format(y, m, d))
        self.assertEquals(y, 2014)
        self.assertEquals(m, 2)
        self.assertEquals(d, 11)

    def test4(self):
        # 27-Feb-6700 12Uhr, 4168242
        y, m, d = jd_to_date(4168242)
        # print("\nDate: {0:04d}-{1:02d}-{2:02d}".format(y, m, d))
        self.assertEquals(y, 6700)
        self.assertEquals(m, 2)
        self.assertEquals(d, 27)

    def test5(self):
        # 28-Feb-6700 12Uhr, 4168243
        y, m, d = jd_to_date(4168243)
        # print("\nDate: {0:04d}-{1:02d}-{2:02d}".format(y, m, d))
        self.assertEquals(y, 6700)
        self.assertEquals(m, 2)
        self.assertEquals(d, 28)

    def test6(self):
        # 01-Mar-6700 12Uhr, 4168244
        y, m, d = jd_to_date(4168244)
        # print("\nDate: {0:04d}-{1:02d}-{2:02d}".format(y, m, d))
        self.assertEquals(y, 6700)
        self.assertEquals(m, 3)
        self.assertEquals(d, 1)

    def test7(self):
        # 02-Mar-6700 12Uhr, 4168245
        y, m, d = jd_to_date(4168245)
        # print("\nDate: {0:04d}-{1:02d}-{2:02d}".format(y, m, d))
        self.assertEquals(y, 6700)
        self.assertEquals(m, 3)
        self.assertEquals(d, 2)


if __name__ == '__main__':
    unittest.main()
