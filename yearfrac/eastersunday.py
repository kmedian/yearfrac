
def eastersunday(y):
    if not isinstance(y, int):
        raise Exception("y is not an integer data type.")
    if (y < 1583) or (y > 4099):
        raise Exception("The year have to be between 1583 and 4099")

    FirstDig = int(y / 100.0)  # first 2 digits of year
    Remain19 = y % 19  # remainder of year / 19

    # calculate PFM date
    temp = 202  # Smallest temp is 202-198-0-2=2
    temp -= (11 * Remain19)  # values up to 198 possible; is less than 202
    temp += int((FirstDig - 15) / 2.0)  # min(FirstDig)=15; MAX=202-0+7=209

    if FirstDig in (21, 24, 25, 27, 28, 29, 30, 31, 32, 34, 35, 38):
        temp -= 1
    elif FirstDig in (33, 36, 37, 39, 40):
        temp -= 2

    temp = temp % 30

    # Compute tA
    tA = temp + 21  # tA cannot be less than 20; MAX=29+21=40

    if temp is 29:
        tA -= 1

    if (temp is 28) and (Remain19 > 10):
        tA -= 1

    # find the next Sunday
    tB = (tA - 19) % 7  # As said, tA cannot be less than 20

    # Compute tC
    tC = (40 - FirstDig) % 4  # Maximum value is FirstDig=40

    if tC is 3:
        tC += 1

    if tC > 1:
        tC += 1

    # Compute tD
    temp = y % 100  # temp is unsigned
    tD = (int(temp / 4.0) + temp) % 7

    # Compute tE
    tE = ((20 - tB - tC - tD) % 7) + 1  # Max tB=6, tC=3, tD=6 ==> 20-6-3-6=5

    # Compute Day d
    d = tA + tE

    # adjust March vs April
    m = 3
    if d > 31:
        d -= 31
        m = 4

    # done
    return m, d
