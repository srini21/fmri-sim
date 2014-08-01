import numpy as np,os,sys
import matplotlib.pyplot as plt

def sin(num):
    y=np.tanh(num)
    return y

def generate_Z(thetaname,theta,alpha):
    if not os.path.exists('Z_fMRI'):
        os.makedirs('Z_fMRI')
    theta=np.resize(theta,theta.size)
    z=np.dot(alpha.T,theta)
    for i in range(0,z.size):
        z[i]=sin(z[i])
    np.save('Z_fMRI/z'+thetaname,z)
    
def getThetaAlpha(phenotypes):
    #get the number of files
    thetanames=np.load('Theta_fMRI/ThetaFiles.npy')
    for thetaname in thetanames:
        theta=np.load('Theta_fMRI/'+thetaname+'.npy')
        (x,y)=theta.shape
        #maintaining sparsity
        alpha=theta
        alpha[alpha.nonzero()]=np.random.randn(len(alpha[alpha.nonzero()]))
        for i in range(0,phenotypes):
            temp=theta
            temp[temp.nonzero()]=np.random.rand(len(temp[temp.nonzero()]))
            alpha=np.dstack((alpha,temp))
        alpha=np.resize(alpha,(theta.size,phenotypes))
        generate_Z(thetaname,theta,alpha)
def main():
    phenotypes=int(sys.argv[1])
    getThetaAlpha(phenotypes)


if __name__ == '__main__':
    main()
