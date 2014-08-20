import numpy as np
def computeD(type,ysc,x,Ahat,Bhat):
    eta=np.dot(x,Ahat.T)+(np.dot(x,Bhat.T)*ysc).sum(axis=1).reshape(len(np.dot(x,Bhat.T)*ysc),1)
    #eta=eta/max(eta)#Check if this is ok
    if type=='poisson':
        dval=(np.exp(eta)).sum()
    elif type=='gaussian':
        dval=0.5*(eta**2).sum()
    return dval

def computeDgrad(type,ysc,x,Ahat,Bhat):
    (n,p)=ysc.shape
    (n_temp,q)=x.shape
    eta=np.dot(x,Ahat.T)+(np.dot(x,Bhat.T)*ysc).sum(axis=1).reshape(len(np.dot(x,Bhat.T)*ysc),1)
    if type=='poisson':
        temp_Dgrad=np.exp(eta)
    elif type=='gaussian':
        temp_Dgrad=eta

    Bgrad=np.dot((np.kron(temp_Dgrad,np.ones((1,p)))*ysc).T,x)
    Agrad=(np.kron(temp_Dgrad,np.ones((1,q)))*x).sum(axis=0)
    np.save('Agrad',Agrad)
    np.save('Bgrad',Bgrad)
    return (Agrad,Bgrad)

def main():
    Y=np.load('concat_fMRI.npy')
    x=np.load('concat_bs.npy')
    curr=0
    ys=Y[:,curr]
    ysc=np.hstack((Y[:,:curr],Y[:,curr+1:]))
    thr=5e-4
    maxit=1e3
    beta=0.5
    (n,p)=ysc.shape
    (n_temp,q)=x.shape
    (n_temp2)=ys.shape
    yyx=np.dot((np.kron(ys,np.ones((p,1))).T*ysc).T,x)
    ysx=np.dot(ys,x)
    Bhat=np.random.rand(p,q)/q
    Ahat=np.random.rand(1,q)/q
    iter=1
    ind=1
    obj=np.inf
    #while thr<ind and iter<maxit:
    Bold=Bhat
    Aold=Ahat
    (D_Agrad,D_Bgrad)=computeDgrad('gaussian',ysc,x,Ahat,Bhat)
    Bgrad=-(1/float(n))*yyx+(1/float(n))*D_Bgrad
    Agrad=-(1/float(n))*ysx+(1/float(n))*D_Agrad
    t=1
    Btmp = Bold - t*Bgrad
    lambda=t*lam
    num_threads=-1
    regul='l1l2'
    
   
if __name__ == '__main__':
    main()

