# AS4100-1998-Mo_Moment_Calculator
Buckling Moment Calculator for Steel Structures - AS4100:1998

### REPL - View Live CLI Output:
Refer to link below to run the code from Repl.it CLI
https://replit.com/@daveh87/MoCalculator?embed=1#main.py

### Introduction
I am a Structural Engineer from Sydney Australia, i've created a main.py python script to calculate the Alpha_s & Alpha_m values as well as the buckling moment for 
steel members in bending. 

### Setup
The first thing to do is to clone the repository:

> $ git clone https://github.com/daveh07/AS4100-1998-Mo_Moment_Calculator.git

> Py Version: Python 3.9

Create a virtual environment and run main.py

### NOTE:
Please feel free to add any contributions! This is a basic calculation for most common cases of Alpha_S. Further code clauses to be added for alpha_m.  

### What I Learned
<li>Creating a command line script</li>
<li>Using Repl.it to deploy CLI App</li>
<li>Creating user inputs and performing calculations based on input values</li>

### Example Caluclation
Steel Section 460UB82.1 Portal Frame Column
#### Section Properties:
<li> Effective Length (mm), Le = 6000
<li> Moment of Inertia about y-axis - Iy (mm4), Le = 6000
<li> Warping Constant Iw (mm9)= 919000000000
<li> Torsion Constant, J = 701000
<li> Shear Modulus of Elasticity 80x10^3 (MPa), G = 80000
<li> Youngs Modulus of Elasticity, E (MPa) = 200000
<li> Reduction Factor PHI = 0.90  
<li> Section Capacity (kNm) = 551.1  


#### Design Moments (kNm):
<li> M*m = 270
<li> M*2 = 230
<li> M*3 = 175
<li> M*4 = 155  

#### Results:
<li> Buckling Moment = 165.1kNm  
<li> Alpha_m = 1.4  


