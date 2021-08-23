# MEMBER CAPACITY OF SEGMENTS WITHOUT FULL LATERAL RESTRAINT
# IN ACCORDANCE WITH AS4100-1998 - SECTION 5.6
#
# V1.0 - 04/12/2020 by D.HILL
from userInputs import *
from alpha_m import *
from alpha_s import *


# Calculate Alpha M
print("Alpha_m = " + str((alpha_m_moment())))

# Calculate Alpha S
buckling_moment()

