import numpy as np,sys


def usage():
    print "num_nodes behav_ft"
    sys.exit(2)


def generate_w(num_nodes, behav_ft):
    print "---------------------"
    print "generating Wf and Wd"
    print "---------------------"
    G=np.load('adj_mat')
    print G.shape
    Wf=G
    Wf[Wf.nonzero()]=np.random.randn(len(Wf[Wf.nonzero()]))
    for i in range(0,behav_ft+1):
        temp=G
        temp[temp.nonzero()]=np.random.randn(len(temp[temp.nonzero()]))
        Wf=np.dstack((Wf,temp))
    np.save(open('Wf','w'),Wf)
    Wd=G
    Wd[Wd.nonzero()]=np.random.randn(len(Wd[Wd.nonzero()]))
    for i in range(0,behav_ft+1):
        temp=G
        temp[temp.nonzero()]=np.random.randn(len(temp[temp.nonzero()]))
        Wd=np.dstack((Wd,temp))
    np.save(open('Wd','w'),Wd)
    print "Shape of weights"
    print Wd.shape
    print "Done"
        
    

        
def main():
    if len(sys.argv)<2:
        usage()
    
    num_nodes=int(sys.argv[1])
    behav_ft=int(sys.argv[2])
    generate_w(num_nodes,behav_ft)
    
if __name__ == '__main__':
    main()
