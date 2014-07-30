#author : Srinivasan Sivaramachandrannum_nodes=300
num_scans=5
Wd=np.load('Wd')
Wd=np.absolute(Wd/1000)
x=np.load('person0/b19.npy')
burnin=0
sampint=500
tempx=np.zeros((num_nodes,1))
for s in range(0,num_scans):
    if s==1:
        sampleSkip= burnin+sampint
    else:
        sampleSkip=sampint
        for ctr in range(0,sampleSkip):
            for i in range(0,num_nodes):
                theta_true=np.dot(Wd[i,:,:],x)
                eta=sampint + np.dot(theta_true.T,tempx) 
                assert eta>=0
                eta= eta/100
                tempx[i]=np.random.poisson(np.exp(eta))
                samples[s,:]=tempx.T
