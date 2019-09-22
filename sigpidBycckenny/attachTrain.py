from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import numpy as np
import pandas as pd
import csv
import os

class apkToCsv():
    def __init__(self):
        self.permission = []
        self.path = ''
        self.featurePath = ''

    def get_permission(self, path):
        self.path = path
        app = apk.APK(path)
        try:
            self.permission = app.get_permissions()
        except:
            pass
        #print (self.permission)

    def toCsv(self):
        header = ['android.permission.ACCESS_WIFI_STATE', 
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
        init = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        for item in self.permission:
            for index in range(len(header)):
                if item == header[index]:
                    init[index] = 1
        with open("F:\\document\\sigpidBycckenny\\train.csv","a", newline='') as datacsv:
            writer = csv.writer(datacsv)
            writer.writerow(init)
       

if __name__ == '__main__':
    test = apkToCsv()
    search_dir = 'F:\\vsmal\\'
    for root, subdir, filenames in os.walk(search_dir):
        for fn in filenames:
            print(fn) 
            test.get_permission(search_dir + fn)
            test.toCsv()

