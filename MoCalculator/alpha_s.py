import math
from userInputs import *

#--------------------USER INPUTS------------------------#
class alphaSInput:
    def __init__(self):
        self.le = le                        # Effective length of segment/member
        self.iy = iy                        # Moment of Inertia Minor Axis (about y-axis) of segment
        self.iw = iw                        # Warping Constant of segment/member
        self.torsionconst = torsionconst    # Torsion Constant of segment/member
        self.shearmod = shearmod            # Shear Modulus
        self.emod = emod                    # Elastic Modulus
        self.phi = phi                      # Reduction Factor, Phi
        self.msx = msx                      # Section Capacity of segment/member about the major x- axis

# Alpha Mo Calculation
def buckling_moment():
    mo = float(((((math.pi**2)*emod*iy)/(le**2))*((shearmod*torsionconst)+((math.pi**2)*emod*iw)/(le**2)))**0.5) / 10**6
    return round(mo, 2)


print("Buckling Moment, Mo = " + str(buckling_moment()) + "kNm")

# Calculate Alpha M

