from sklearn.svm import SVR
import numpy as np
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
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

lin=SVR(kernel='rbf')

print "true self"
print "fmri"
test_size,phenotypes=yf_train.shape
mae=[]
mse=[]
r2=[]
for i in range(0,phenotypes):
    yf_pred=lin.fit(Xf_train,yf_train[:,i]).predict(Xf_test)
    mae.append(mean_absolute_error(yf_pred,yf_test[:,i]))
    mse.append(mean_squared_error(yf_pred,yf_test[:,i]))
    r2.append((r2_score(yf_test[:,i],lin.fit(Xf_train,yf_train[:,i]).predict(Xf_test))))
print "mae:"+str(np.mean(mae))
print "mse:"+str(np.mean(mse))
print "r2:"+str(np.mean(r2))

print "dti"
mae=[]
mse=[]

for i in range(0,phenotypes):
    yd_pred=lin.fit(Xd_train,yd_train[:,i]).predict(Xd_test)
    mae.append(mean_absolute_error(yd_pred,yd_test[:,i]))
    mse.append(mean_squared_error(yd_pred,yd_test[:,i]))
    r2.append((r2_score(yd_test[:,i],lin.fit(Xd_train,yd_train[:,i]).predict(Xd_test))))
print "mae:"+str(np.mean(mae))
print "mse:"+str(np.mean(mse))
print "r2:"+str(np.mean(r2))
print "fmri_w_comput"
mae=[]
mse=[]

for i in range(0,phenotypes):
    yf_est_pred=lin.fit(Xf_est_train,yf_est_train[:,i]).predict(Xf_est_test)
    mae.append(mean_absolute_error(yf_est_pred,yf_est_test[:,i]))
    mse.append(mean_squared_error(yf_est_pred,yf_est_test[:,i]))
    r2.append((r2_score(yf_est_test[:,i],lin.fit(Xf_est_train,yf_est_train[:,i]).predict(Xf_est_test))))
print "mae:"+str(np.mean(mae))
print "mse:"+str(np.mean(mse))
print "r2:"+str(np.mean(r2))
print "dti_w_comput"
mae=[]
mse=[]

for i in range(0,phenotypes):
    yd_est_pred=lin.fit(Xd_est_train,yd_est_train[:,i]).predict(Xd_est_test)
    mse.append(mean_squared_error(yd_est_pred,yd_est_test[:,i]))
    mae.append(mean_absolute_error(yd_est_pred,yd_est_test[:,i]))
    r2.append((r2_score(yd_est_test[:,i],lin.fit(Xd_est_train,yd_est_train[:,i]).predict(Xd_est_test))))
print "mae:"+str(np.mean(mae))
print "mse:"+str(np.mean(mse))
print "r2:"+str(np.mean(r2))
