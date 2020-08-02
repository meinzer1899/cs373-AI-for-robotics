# CORRECT INTIALIZATION

P =  matrix([[1000., 0.], [0., 1000.]])# initial uncertainty: 0 for positions x and y, 1000 for the two velocities
F =  matrix([[1., 0., dt, 0.], [0., 1., 0., dt],[0., 0., 1., 0.],[0., 0., 0., 1.]])# next state function: generalize the 2d version to 4d
H =  matrix([[1., 1., 0., 0.]])# measurement function: reflect the fact that we observe x and y but not the two velocities
R =  matrix([[0.1, 0.], [0., 0.1]])# measurement uncertainty: use 2x2 matrix with 0.1 as main diagonal
I =  matrix([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])# 4d identity matrix


