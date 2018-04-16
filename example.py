# example code to calculate Lhat and nhat from the waveform for a simulation

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math as mt

from transformation_functions import *
from ln_steps import *

# load in psi4,2m modes as a 2d array
# in the form 3 columns; time | Re psi4 | Im psi4

psi4_22  =
psi4_21  = 
psi4_20  = 
psi4_2m1 = 
psi4_2m2 = 

# set initial time (just after passage of junk radiation at origin of simulation)

junk_time = 0

# give radius at which waveform data was extracted 
# this should correspond to the timeshift between the dynamics and waveform data

ext_rad = 0

# set simulation type - based on conventions used when producing waveform
# can take value 'BAM' or 'SXS'

simulation_type = SXS


# give initial guess of Newtonian orbital angular momentum (optional) -- if not specified will default to value (0, 0, 1)

#LN_guess = 


# call function to calculate Lhat and nhat
# need to specify which code was used to produce the waveform - e.g. 'BAM'

L, n =  all_steps(psi4_22, psi4_21, psi4_20, psi4_2m1, psi4_2m2, junk_time, ext_rad, simulation_type, LN_guess)


# write results to file

f1 = open("L.txt","w")
f1.write("time (M) \t\t\t Lx \t\t\t Ly \t\t\t Lz \n")
np.savetxt(f1,L,delimiter='\t')
f1.close()

f2 = open("n.txt","w")
f2.write("time (M) \t\t\t nx \t\t\t ny \t\t\t nz \n")
np.savetxt(f2,n,delimiter='\t')
f2.close()
