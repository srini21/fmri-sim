import numpy as np,os
import matplotlib.pyplot as plt

def sin(num):
    y=np.sin(num)
    return y

def generate_Z(thetaname,theta,alpha,x,y):
    if not os.path.exists('Z_fMRI'):
        os.makedirs('Z_fMRI')
    z=np.dot(theta,alpha)
    for i in range(0,x):
        for j in range(0,y):
            z[i,j]=sin(z[i,j])#Sin explicitly defined so that the function can be changed. 
    np.save('Z_fMRI/z'+thetaname,z)
    
def getThetaAlpha():
    #get the number of files
    thetanames=np.load('Theta_fMRI/ThetaFiles.npy')
    for thetaname in thetanames:
        theta=np.load('Theta_fMRI/'+thetaname+'.npy')
        (x,y)=theta.shape
        alpha=np.random.rand(x,y)
        generate_Z(thetaname,theta,alpha,x,y)
def main():
    getThetaAlpha()


if __name__ == '__main__':
    main()
