import numpy as np,os,sys

def generate_samplesfmri(num_ppl,num_nodes,num_scans):
    print "-----------------------"
    print "generating fMRI samples"
    print "-----------------------"
    if not os.path.exists('Samples_fMRI'):
        os.makedirs('Samples_fMRI')
    ppl=range(0,num_ppl)
    Wf=np.load('Wf')
    count=0
    for i in ppl:
        dir='person'+str(i)
        ages=np.load(dir+'/age')
        for age in ages:
            X=np.load(dir+'/b'+str(age)+'.npy')
            theta=np.dot(Wf,X)
            Y=np.random.multivariate_normal([0]*num_nodes,theta,num_scans)
            filename='yf_'+str(i)+'_'+str(age)
            np.save('Samples_fMRI/'+filename,Y.T)
            count=count+1
    count=count*num_scans
    print str(count)+" Samples of fMRI created"

def generate_samplesdti(num_ppl,num_nodes, num_scans): 
    print "-----------------------"
    print "generating dti samples"
    print "-----------------------"
    if not os.path.exists('Samples_dti'):
        os.makedirs('Samples_dti')   
    Wd=np.load('Wd')
    count=0
    ppl=range(0,num_ppl)
    for i in ppl:
        dir='person'+str(i)
        ages=np.load(dir+'/age')
        for age in ages:
            X=np.load(dir+'/b'+str(age)+'.npy')
            filename='yd_'+str(i)+'_'+str(age)
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
                            theta_true=np.dot(w[i,:,:],x)
                            eta=sampint + np.dot(theta_true.T,tempx)
                            assert eta>=0
                            eta= eta/100
                            tempx[i]=np.random.poisson(np.exp(eta))
            samples[s,:]=tempx.T
            np.save('Samples_dti/'+filename,samples)
            count=count+1
    count=count*num_scans
    print str(count)+" samples of dti generated"
    

def usage():
    print "num_ppl num_nodes num_scans"
    sys.exit(2)

def main():
    if len(sys.argv) < 2:
        usage()
    num_ppl=int(sys.argv[1])
    num_nodes=int(sys.argv[2])
    num_scans=int(sys.argv[3])
    generate_samplesfmri(num_ppl,num_nodes, num_scans)
    generate_samplesdti(num_ppl,num_nodes,num_scans)



if __name__ == '__main__':
    main()
