
def date_to_jd(year: int, month: int, day: int) -> int:
    a = int((14 - month) / 12.)
    y = int(year + 4800 - a)
    m = int(month + (12 * a) - 3)

    jd = day + int(((153 * m) + 2) / 5.0) + (y * 365)
    jd += int(y / 4.) - int(y / 100.) + int(y / 400.) - 32045
    return jd


def jd_to_date(jd: int) -> (int, int, int):
    a = jd + 32044
    b = int(((4 * a) + 3) / 146097.)
    c = a - int((b * 146097) / 4.)

    d = int(((4 * c) + 3) / 1461.)
    e = c - int((d * 1461) / 4.)
    m = int(((5 * e) + 2) / 153.)
    m2 = int(m / 10)

    day = e + 1 - int(((153 * m) + 2) / 5.)
    month = (m + 3 - (12 * m2))
    year = ((b * 100) + d - 4800 + m2)

    return year, month, day
