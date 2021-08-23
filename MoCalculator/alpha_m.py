# MEMBER CAPACITY OF SEGMENTS WITHOUT FULL LATERAL RESTRAINT
# IN ACCORDANCE WITH AS4100-1998 - SECTION 5.6
#
# V1.0 - 04/12/2020 by D.HILL


# Alpha M Parameters
mm = input("M*m = ")
mm = float(mm)
m2 = input("M*2 = ")
m2 = float(m2)
m3 = input("M*3 = ")
m3 = float(m3)
m4 = input("M*4 = ")
m4 = float(m4)
    

# Calculate Alpha M
def alpha_m_moment():
    alpha_m = (1.7 * mm) / (((m2 ** 2) + (m3 ** 2) + (m4 ** 2)) ** 0.5)
    if alpha_m <= 2.5:
        alpha_m = alpha_m
    else:
        alpha_m = 2.5

    return round(alpha_m, 3)


class Alpha_m:
    pass


# print(Alpha_m.alpha_m_moment())


