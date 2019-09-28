def d30360e(y1: int, m1: int, d1: int,
            y2: int, m2: int, d2: int, matu: bool) -> float:

    diff_days = 0
    diff_days += (360 * (y2 - y1))
    diff_days += (30 * (m2 - m1))
    if (m2 == 2) and (d2 >= 28):
        if matu:
            diff_days += d2
        else:
            diff_days += 30
    else:
        diff_days += 30 if d2 > 30 else d2

    if (m1 == 2) and (d1 >= 28):
        diff_days -= 30
    else:
        diff_days -= 30 if d1 > 30 else d1

    if diff_days < 0:
        raise Exception(
            'Newer date y2-m2-d2 is older than previous date y1-m1-d1.')
    elif diff_days == 0:
        return 0e0
    else:
        return diff_days / 360e0
