#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Binoy.Pilakkat
#
# Created:     09/08/2013
# Copyright:   (c) Binoy.Pilakkat 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, math
def solve(m, k, beta, S0, dt, g,  N):
    S = [0.0]*(N+1) # output list
    gamma = beta*dt/2.0 # short form
    t = 0
    S[0] = S0
    # special formula for first time step:
    i = 0
    S[i+1] = (1/(2.0*m))*(2*m*S[i] - dt**2*k*S[i] + m*(math.cos(t+dt) - 2*math.cos(t) + math.cos(t-dt)) + dt**2*m*g)
##    S[i+1] = (1/(2.0*m))*(2*m*S[i] - dt**2*k*S[i] +  dt**2*m*g)
    t = dt
    for i in range(1,N):
##        S[i+1] = (1/(m + gamma))*(2*m*S[i] - m*S[i-1] + gamma*dt*S[i-1] - dt**2*k*S[i] + dt**2*m*g)
        S[i+1] = (1/(m + gamma))*(2*m*S[i] - m*S[i-1] + gamma*dt*S[i-1] - dt**2*k*S[i] + m*(math.cos(t+dt) - 2*math.cos(t) + math.cos(t-dt))+ dt**2*m*g)
        t += dt
    return S
from math import pi
m = 1; b = 2; L = 100; k = 10; beta = 0.5; S0 = 2;
dt = 2*pi/60; g = 11; w_formula = 'sin'; N = 500;

S = solve(m, k, beta, S0, dt, g,  N)


##s = 'My {1[spam]:<9} runs {0.platform:>8}'.format(sys ,{'spam':'laptop'})
Xmax = max(S)
Xmin = min(S)
XX = Xmax+Xmin

Step = 100/(max(S)-min(S))


for i in S:
    d= -(Xmin*Step)+(Step * i)
    s = '{0}{1}'.format(int(d)*' ','X')
    print s
r = raw_input("")