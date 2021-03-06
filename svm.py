from sklearn.ensemble import RandomForestRegressor
from sklearn.grid_search import GridSearchCV
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

lin=RandomForestRegressor(n_estimators=10)
print 'fmri'
yf_pred=lin.fit(Xf_train,np.ravel(yf_train)).predict(Xf_test)
print mean_absolute_error(yf_pred,yf_test)
print mean_squared_error(yf_pred,yf_test)
print r2_score(yf_test,yf_pred)
print 'fmri w_comput'
yf_pred=lin.fit(Xf_est_train,np.ravel(yf_est_train)).predict(Xf_est_test)
print mean_absolute_error(yf_pred,yf_est_test)
print mean_squared_error(yf_pred,yf_est_test)
print r2_score(yf_est_test,yf_pred)
print 'dti'
yd_pred=lin.fit(Xd_train,np.ravel(yd_train)).predict(Xd_test)
print mean_absolute_error(yd_pred,yd_test)
print mean_squared_error(yd_pred,yd_test)
print r2_score(yd_test,yd_pred)
print 'dti w_comput'
yd_pred=lin.fit(Xd_est_train,np.ravel(yd_est_train)).predict(Xd_est_test)
print mean_absolute_error(yd_pred,yf_est_test)
print mean_squared_error(yd_pred,yd_est_test)
print r2_score(yd_est_test,yd_pred)

