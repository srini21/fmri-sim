import numpy as np
import networkx as nx
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

wf=np.load('Wf')
wd=np.load('Wd')
wfc=np.load('Wf_comput.npy')
wdc=np.load('Wd_comput.npy')
a,b,c=wf.shape
r2=[]
print "fMRI"
print "Mean square error: " + str(np.linalg.norm(wf-wfc)/np.size(wf))
print "Relative error   : " + str(np.linalg.norm(wf-wfc)/np.linalg.norm(wf))
print "r2 score         : "
print r2_score(np.reshape(wf,np.size(wf)),np.reshape(wfc,np.size(wfc)))
print "----------------"
r2=[]
print "dti"
print "Mean square error: "+str(np.linalg.norm(wd-wdc)/np.size(wd))
print "Relative error   : "+str(np.linalg.norm(wd-wdc)/np.linalg.norm(wd))
print "r2 score         : " 
print r2_score(np.reshape(wd,np.size(wd)),np.reshape(wdc,np.size(wdc)))
print "----------------"

tofGraph=wfc[:,:,1]
tofGraph[tofGraph<0]=0
todGraph=wdc[:,:,1]
todGraph[todGraph<0]=0
adjmat=np.load('adj_mat')
G=nx.from_numpy_matrix(adjmat)
G2=nx.from_numpy_matrix(tofGraph)
G3=nx.from_numpy_matrix(todGraph)
fig1=plt.figure()
nx.draw(G)
plt.savefig('Original.png')
fig2=plt.figure()
nx.draw(G2)
plt.savefig('fmri_est.png')
fig3=plt.figure()
nx.draw(G3)
plt.savefig('dti_est.png')
