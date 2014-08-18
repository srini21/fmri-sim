#author : Srinivasan Sivaramachandran
#Concatenates the samples based on the index information from Theta_dti/ThetaFiles.npy
import numpy as np, os, sys


def concat(type):
    f_files=np.load('Theta_fMRI/ThetaFiles.npy')
    d_files=np.load('Theta_dti/ThetaFiles.npy')
    flag=True
    if type=='fMRI':
        file=f_files
    else:
        file=d_files
    for i in file:      
        y=np.load('Samples_'+type+'/'+i[3:]+'.npy')
        if flag:
            wholeColl=y
            flag=False
        else:
            wholeColl=np.hstack((wholeColl,y))
    np.save('concat_'+type,wholeColl.T)

def concat_b(num_ppl,num_scans):
    ppl=range(0,num_ppl)
    flag=True
    for i in ppl:
        dir='person'+str(i)
        ages=np.load(dir+'/age')
        for age in ages:
            X=np.load(dir+'/b'+str(age)+'.npy')
            temp=X
            temp.resize(len(X),1)
            temp=np.tile(temp,num_scans)
            if flag:
                bs=temp
                flag=False
            else:
                bs=np.hstack((bs,temp))
    np.save('concat_bs',bs.T)

def usage():
    print "num_ppl num_scans"
    sys.exit(2)

def main():
    if len(sys.argv) < 2:
        usage()
    concat('fMRI')
    concat('dti')
    num_ppl=int(sys.argv[1])
    num_scans=int(sys.argv[2])
    concat_b(2,3)
if __name__ == '__main__':
    main()

    
