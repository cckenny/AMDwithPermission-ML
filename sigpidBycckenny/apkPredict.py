from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
from sklearn.externals import joblib
import csv
import os

class apkToCsv():
    def __init__(self):
        self.permission = []
        self.path = ''
        self.featurePath = ''
        self.count = 0
        self.header = ['android.permission.ACCESS_WIFI_STATE', 
		'android.permission.CAMERA', 
		'android.permission.CHANGE_NETWORK_STATE', 
		'android.permission.CHANGE_WIFI_STATE', 
		'android.permission.DISABLE_KEYGUARD', 
		'android.permission.GET_TASKS', 
		'android.permission.INSTALL_PACKAGES', 
		'android.permission.READ_CALL_LOG', 
		'android.permission.READ_CONTACTS', 
		'android.permission.READ_EXTERNAL_STORAGE', 
		'com.android.browser.permission.READ_HISTORY_BOOKMARKS',
		'android.permission.READ_LOGS', 
		'android.permission.READ_PHONE_STATE', 
		'android.permission.READ_SMS', 
		'android.permission.RECEIVE_BOOT_COMPLETED', 
		'android.permission.RESTART_PACKAGES', 
		'android.permission.SEND_SMS', 
		'android.permission.SET_WALLPAPER', 
		'android.permission.SYSTEM_ALERT_WINDOW', 
		'android.permission.WRITE_APN_SETTINGS', 
		'android.permission.WRITE_CONTACTS', 
		'android.permission.WRITE_SETTINGS',
		'class']
        self.init = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def get_permission(self, path):
        self.path = path
        app = apk.APK(path)
        self.permission = app.get_permissions()
        #print (self.permission)

    def toCsv(self):
        self.init = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for item in self.permission:
            for index in range(len(self.header)):
                if item == self.header[index]:
                    self.init[index] = 1
        print(self.init)
        self.featurePath = self.path + '.csv'
        test = pd.DataFrame(columns = self.header, data = [self.init])
        test.to_csv(self.featurePath, index = False)
       
    def predict(self):
        rawdata = pd.read_csv(self.featurePath)
        T = rawdata.iloc[:,0:22]
        testdata = np.array(T)
        model = joblib.load('rf.model')
        # make predictions
        predicted = model.predict(testdata)
        print(predicted)
        if predicted == [0]:
            self.count += 1
        rawdata = rawdata.drop(labels = 0)
        self.init[22] = predicted[0]
        test = pd.DataFrame(columns = self.header, data = [self.init])
        test.to_csv(self.featurePath, index = False)

if __name__ == '__main__':
    test = apkToCsv()
    search_dir = r'F:\download\Benign-APKs\\'
    for root, subdir, filenames in os.walk(search_dir):
        for fn in filenames:
            test.get_permission(search_dir + fn)
            test.toCsv()
            test.predict()
    print(str(test.count)+'检测为良性') 

