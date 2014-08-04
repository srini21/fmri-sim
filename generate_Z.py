import numpy as np,os,sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def sin(num):
    y=1/(1+np.exp(-num))
    return y

def generate_Z(thetaname,theta,alpha):
    if not os.path.exists('Z_fMRI'):
        os.makedirs('Z_fMRI')
    theta=np.resize(theta,theta.size)
    z=np.dot(alpha.T,theta)
    for i in range(0,z.size):
        z[i]=sin(z[i])
    for i in range(0,z.size):
        z[i]=(z[i]-np.mean(z))/np.std(z)
    return z
    
def getThetaAlpha(phenotypes):
    #get the number of files
    thetanames=np.load('Theta_fMRI/ThetaFiles.npy')
    z=[]
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
        z.extend(generate_Z(thetaname,theta,alpha))
    np.save('Z',z)
    plt.hist(z,normed=True)
    plt.savefig('2sig.png')
def main():
    phenotypes=int(sys.argv[1])
    getThetaAlpha(phenotypes)


if __name__ == '__main__':
    main()
