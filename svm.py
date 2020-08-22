#Author: Manu Gupta
#Feel Free to Use this Code as You Like :)
#Also, sorry for the excessive comments, but this code was originally used in a blog post for educational purposes

import random
import matplotlib.pyplot as plt
import numpy as np

#Just some hyper-parameters
NUM_POINTS = 50
DIMENSIONS = 2
X_MAX, Y_MAX = 10, 10

#Preparing my data in a way where it can be plotted and linearly separable
Red_Dots, Green_Dots = [],[]
for i in range(DIMENSIONS):
    Temp = []
    for i in range(NUM_POINTS):
        Temp.append(random.uniform(X_MAX * 0.05, X_MAX * 0.45))
    Red_Dots.append(Temp)
for i in range(DIMENSIONS):
    Temp = []
    for i in range(NUM_POINTS):
        Temp.append(random.uniform(X_MAX * 0.55, X_MAX * 0.95))
    Green_Dots.append(Temp)

#Plotting the points and graphing it
plt.plot(Red_Dots[0], Red_Dots[1], 'ro')
plt.plot(Green_Dots[0], Green_Dots[1], 'go')
plt.axis([0, X_MAX, 0, Y_MAX])

#The hardest issue with SVM is having two equidistant support vectors, so first we have to choose random ones
r = random.randint(0,NUM_POINTS-1)
Red_SV, Green_SV = [], []
for i in range(DIMENSIONS):
    Red_SV.append(Red_Dots[i][r])
    Green_SV.append(Green_Dots[i][r])

#We find the midpoint of the support vectors as that point will be on our boundary
Midpoint = []
for i in range(DIMENSIONS):
    Midpoint.append((Red_SV[i]+Green_SV[i])/2)

#Now, we use the formula we derived for the weights in the blog post, namely labels (we will label red positive and green negative)
Weights = []
for i in range(DIMENSIONS):
    Weights.append(Red_SV[i]-Green_SV[i])

#We will now calculate the bias, namely b = -w^Tx, assuming our midpoint is on the line w^Tx+b = 0. Because of how we implemented our code
#support vectors first instead of a random line we don't have to do b = L-w^Tx_s. In reality, the concept still remains the same.
Bias = 0
for i in range(DIMENSIONS):
    Bias -= Weights[i]*Midpoint[i]

#Our line works, but to choose the optimal support vectors, we can go through each array of points and find the lowest distance through the formula in the blog
Weight_Magnitude = 0
for i in range(DIMENSIONS):
    Weight_Magnitude += Weights[i]**2
Weight_Magnitude = Weight_Magnitude**0.5

Min_RD, Min_GD = X_MAX + Y_MAX, X_MAX + Y_MAX
Red_SV, Green_SV = [], []
for i in range(NUM_POINTS):
    R_Distance, G_Distance = 0, 0
    for j in range(DIMENSIONS):
        R_Distance += Weights[j]*Red_Dots[j][i]
        G_Distance += Weights[j]*Green_Dots[j][i]
    R_Distance = abs((R_Distance + Bias)/Weight_Magnitude)
    G_Distance = abs((G_Distance + Bias)/Weight_Magnitude)
    if R_Distance < Min_RD:
        Min_RD = R_Distance
        Red_SV = []
        for j in range(DIMENSIONS):
            Red_SV.append(Red_Dots[j][i])
    if G_Distance < Min_GD:
        Min_GD = G_Distance
        Green_SV = []
        for j in range(DIMENSIONS):
            Green_SV.append(Green_Dots[j][i])

#Now, we have better support vectors, we just rinse and repeat
Midpoint, Weights, Bias = [], [], 0
for i in range(DIMENSIONS):
    Midpoint.append((Red_SV[i]+Green_SV[i])/2)
    Weights.append(Red_SV[i]-Green_SV[i])
    Bias -= Weights[i]*Midpoint[i]

#Plotting the line
x = np.linspace(0,X_MAX)
y = (-Bias - Weights[0]*x)/Weights[1]
plt.plot(x,y)
plt.show()

#What I basically did was use a roundabout way of doing SVM with Lagrangian Optimization and 2 Support Vectors.
#I used a hard margin, but for soft margins SGD might be a better form of optimization
