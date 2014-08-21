import numpy as np
import spams
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
    #print np.dot((np.kron(temp_Dgrad,np.ones((1,p)))*ysc).T,x).shape
    #print np.kron(temp_Dgrad,np.ones((1,p)).shape
    Agrad=(np.kron(temp_Dgrad,np.ones((1,q)))*x).sum(axis=0)
    print "Computed with no errors"
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
    lam2=1
    print Bhat.shape
    print Ahat.shape
    while thr<ind and iter<maxit:
        Bold=Bhat
        Aold=Ahat
        (D_Agrad,D_Bgrad)=computeDgrad('gaussian',ysc,x,Ahat,Bhat)
        Bgrad=-(1/float(n))*yyx+(1/float(n))*D_Bgrad
        Agrad=-(1/float(n))*ysx+(1/float(n))*D_Agrad
        t=1
        Btmp = Bold - t*Bgrad
        Bhat=spams.proximalFlat(np.asfortranarray(Btmp),regul='l1l2')
        G_b=(Bold-Bhat)/t
        lam=100
        lam2=200
        Atmp=Aold-t*Agrad
        Ahat=np.reshape(np.append(Atmp[0,0],np.sign(Atmp[0,1:])*np.amax(np.absolute(Atmp[0,0:])-lam2*t,0)),(1,32))
        G_a=(Aold-Ahat)/t
        g_x= -(1/float(n))*((yyx*Bold).sum(axis=0)).sum(axis=0)-(1/float(n))*computeD('gaussian',ysc,x,Aold,Bold)        
        while (((-1/float(n))*yyx*Bhat).sum(axis=0)).sum(axis=0)-(1/float(n))*np.dot(ysx,Ahat.T)+((1/float(n))*computeD('gaussian',ysc,x,Ahat,Bhat)) > g_x-t*np.dot((Bgrad.reshape(np.size(Bgrad),1)).T,G_b.reshape(np.size(G_b),1))+np.dot(Agrad,G_a.T)+(float(t)/2)*np.dot(G_b.reshape(np.size(G_b),1).T,G_b.reshape(np.size(G_b),1))+np.dot(G_a,G_a.T):
            t=beta*t
            Btmp=Bold-t*Bgrad
            Bhat=spams.proximalFlat(np.asfortranarray(Btmp),regul='l1l2')
            G_b=(Bold-Bhat)/t
            Atmp=Aold-t*Agrad
            Ahat=np.reshape(np.append(Atmp[0,0],np.sign(Atmp[0,1:])*np.amax(np.absolute(Atmp[0,0:])-lam2*t,0)),(1,32))
            G_a=(Aold-Ahat)/t
        iter=iter+1
        cur_obj=(((-1/float(n))*yyx*Bhat).sum(axis=0)).sum(axis=0)-(1/float(n))*np.dot(ysx,(Ahat.T))+(1/float(n))*computeD('gaussian',ysc,x,Ahat,Bhat)+lam*(np.sqrt((Bhat**2).sum(axis=1))).sum(axis=0)+lam2*np.linalg.norm(Ahat[0,1:],2)
        
        obj=np.vstack((obj,cur_obj))
        ind=np.linalg.norm(np.vstack((Ahat,Bhat))-np.vstack((Aold,Bold)),'fro')/np.linalg.norm(np.vstack((Aold,Bold)),'fro')

    
if __name__ == '__main__':
    main()
    
