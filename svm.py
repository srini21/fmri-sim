import sklearn.linear_model as lr
import numpy as np
from sklearn.cross_validation import train_test_split

Xd=np.load('concat_dti.npy')
Xf=np.load('concat_fMRI.npy')
yf=np.load('Z_fmri.npy').T
yd=np.load('Z_dti.npy').T
Xd_est=np.load('concat_dti.npy')
Xf_est=np.load('concat_est_fMRI.npy')
yf_est=np.load('Z_est_fmri.npy').T
yd_est=np.load('Z_est_dti.npy').T

Xd_train, Xd_test, yd_train, yd_test= train_test_split(Xd,yd,train_size=0.8,test_size=.2,random_state=0)

Xd_est_train, Xd_est_test, yd_est_train, yd_est_test= train_test_split(Xd_est,yd_est,train_size=0.8,test_size=.2,random_state=0)


Xf_train, Xf_test, yf_train, yf_test= train_test_split(Xf,yf,train_size=0.8,test_size=.2,random_state=0)

Xf_est_train, Xf_est_test, yf_est_train, yf_est_test= train_test_split(Xf_est,yf_est,train_size=0.8,test_size=.2,random_state=0)

lin=lr.LinearRegression()

print "true self"
print "fmri"
print lin.fit(Xf_train,yf_train).score(Xf_test,yf_test)
print "dti"
print lin.fit(Xd_train,yd_train).score(Xd_test,yd_test)

print "true est"
print "fmri"
print lin.fit(Xf_est_train,yf_est_train).score(Xf_est_test,yf_est_test)
print "dti"
print lin.fit(Xd_est_train,yd_est_train).score(Xd_est_test,yd_est_test)

print "train in self and predict in est"
print "fmri"
print lin.fit(Xf_train,yf_train).score(Xf_est_test,yf_est_test)
print "dti"
print lin.fit(Xd_train,yd_train).score(Xd_est_test,yd_est_test)


print "train in est and predict in self"
print "fmri"
print lin.fit(Xf_est_train,yf_est_train).score(Xf_test,yf_test)
print "dti"
print lin.fit(Xd_est_train,yd_est_train).score(Xd_test,yd_test)

