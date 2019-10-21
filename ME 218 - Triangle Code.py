import numpy as np
import sympy as sym
import random

def Coefficient_Matrix(I,I_1,I_2,x_I,y_I,x_I_1,y_I_1,x_I_2,y_I_2):
    A = []
    P = np.matrix([[x_I,y_I,1],[x_I_1,y_I_1,1],[x_I_2,y_I_2,1]])
    detP = np.linalg.det(P)
    
##    phi_I = (x*(P[1,1]-P[2,1])+y*(P[2,0]-P[1,0])+(P[1,0]*P[0,1]-P[2,0]*P[1,1]))/detP
##    phi_I_1 = (x*(P[2,1]-P[0,1])+y*(P[0,0]-P[2,0])+(P[2,0]*P[0,1]-P[0,0]*P[2,1]))/detP
##    phi_I_2 = (x*(P[0,1]-P[1,1])+y*(P[1,0]-P[0,0])+(P[0,0]*P[1,1]-P[1,0]*P[0,1]))/detP
    
    d_phi_I_dx = (P[1,1]-P[2,1])/detP
    d_phi_I_1_dx = (P[2,1]-P[0,1])/detP
    d_phi_I_2_dx = (P[0,1]-P[1,1])/detP
    d_phi_I_dy = (P[2,0]-P[1,0])/detP
    d_phi_I_1_dy = (P[0,0]-P[2,0])/detP
    d_phi_I_2_dy = (P[1,0]-P[0,0])/detP

    A = np.append(A,-1/(detP)**2*(d_phi_I_dx**2+d_phi_I_dy**2))
    A = np.append(A,-1/(detP)**2*(d_phi_I_1_dx*d_phi_I_dx+d_phi_I_1_dy*d_phi_I_dy))
    A = np.append(A,-1/(detP)**2*(d_phi_I_2_dx*d_phi_I_dx+d_phi_I_2_dy*d_phi_I_dy))
    A = np.append(A,-1/(detP)**2*(d_phi_I_1_dx*d_phi_I_dx+d_phi_I_1_dy*d_phi_I_dy))
    A = np.append(A,-1/(detP)**2*(d_phi_I_1_dx**2+d_phi_I_1_dy**2))
    A = np.append(A,-1/(detP)**2*(d_phi_I_2_dx*d_phi_I_1_dx+d_phi_I_2_dy*d_phi_I_1_dy))
    A = np.append(A,-1/(detP)**2*(d_phi_I_2_dx*d_phi_I_dx+d_phi_I_2_dy*d_phi_I_dy))
    A = np.append(A,-1/(detP)**2*(d_phi_I_2_dx*d_phi_I_1_dx+d_phi_I_2_dy*d_phi_I_1_dy))
    A = np.append(A,-1/(detP)**2*(d_phi_I_2_dx**2+d_phi_I_2_dy**2)) 

    A = A.reshape(3,3)
    
    print(A)

Coefficient_Matrix(3,2,4,1.315,0.76,0,0,2.63,0)

##def Equation(a,Q,T,element):
##    T_array = []
##    for i in range(element,element+2):
##        T_array = np.apppend(T_array,T[i])
##    T_matrix = T_matrix.reshape(3,1)
