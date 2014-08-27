import numpy as np,os,sys

def sigmoid(num):
    y=1/(1+np.exp(-num))
    return y

def generate_Z(thetaname,theta,alpha):
    if not os.path.exists('Z_est_fMRI'):
        os.makedirs('Z_est_fMRI')
    theta=np.resize(theta,theta.size)
    z=np.dot(alpha.T,theta)
    for i in range(0,z.size):
        z[i]=sigmoid(z[i])
    for i in range(0,z.size):
        z[i]=(z[i]-np.mean(z))/np.std(z)
    return z
    
def getThetaAlpha(phenotypes,num_scans):
    #get the number of files
    thetanames=np.load('Theta_est_fMRI/ThetaFiles.npy')
    z=[]
    scans=range(0,num_scans)
    for thetaname in thetanames:
        for scan in scans:
            theta=np.load('Theta_est_fMRI/'+thetaname+'.npy')
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
    z=np.reshape(z,(phenotypes,len(thetanames)*num_scans))
    print z
    np.save('Z_est_fmri',z)
    z=[]
    thetanames=np.load('Theta_est_dti/ThetaFiles.npy')
    for thetaname in thetanames:
        for scan in scans:
            theta=np.load('Theta_est_dti/'+thetaname+'.npy')
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
    z=np.reshape(z,(phenotypes,len(thetanames)*num_scans))
    print z
    np.save('Z_est_dti',z)
    
def main():
    phenotypes=int(sys.argv[1])
    num_scans=int(sys.argv[2])
    getThetaAlpha(phenotypes,num_scans)


if __name__ == '__main__':
    main()
