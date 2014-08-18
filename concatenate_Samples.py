#author : Srinivasan Sivaramachandran
#Concatenates the samples based on the index information from Theta_dti/ThetaFiles.npy
import numpy as np, os, sys


f_files=np.load('Theta_fMRI/ThetaFiles.npy')
d_files=np.load('Theta_dti/ThetaFiles.npy')
def concat(type):
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

def main():
    concat('fMRI')
    concat('dti')

if __name__ == '__main__':
    main()

    
