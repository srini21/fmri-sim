import numpy as np,os,sys

def generate_samples(num_ppl,num_nodes,num_scans):
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
            filename='y_'+str(i)+'_'+str(age)
            np.save('Samples_fMRI/'+filename,Y.T)
            count=count+1
    count=count*num_scans
    print str(count)+" Samples of fMRI created"
        

def usage():
    print "num_ppl num_nodes num_scans"
    sys.exit(2)

def main():
    if len(sys.argv) < 2:
        usage()
    num_ppl=int(sys.argv[1])
    num_nodes=int(sys.argv[2])
    num_scans=int(sys.argv[3])
    generate_samples(num_ppl,num_nodes, num_scans)



if __name__ == '__main__':
    main()
