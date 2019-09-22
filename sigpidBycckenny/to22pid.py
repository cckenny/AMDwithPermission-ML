import pandas as pd 
import csv
import re

class sigpid():
	def __init__(self):
		self.listNew = ['android.permission.ACCESS_WIFI_STATE', 
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
		self.listOld = ['ACCESS_WIFI_STATE',
		'CAMERA',
		'CHANGE_NETWORK_STATE',
		'CHANGE_WIFI_STATE',
		'DISABLE_KEYGUARD',
		'GET_TASKS',
		'INSTALL_PACKAGES',
		'READ_CALL_LOG',
		'READ_CONTACTS',
		'READ_EXTERNAL_STORAGE',
		'READ_HISTORY_BOOKMARKS',
		'READ_LOGS',
		'READ_PHONE_STATE',
		'READ_SMS',
		'RECEIVE_BOOT_COMPLETED',
		'RESTART_PACKAGES',
		'SEND_SMS',
		'SET_WALLPAPER',
		'SYSTEM_ALERT_WINDOW',
		'WRITE_APN_SETTINGS',
		'WRITE_CONTACTS',
		'WRITE_SETTINGS']
	def replace(self, dirin, dirout):
		f1 = open(dirin, "r")
		f2 = open(dirout, "w")
		for line in f1:
			for one in range(0, 22):
				if self.listOld[one] in line:
					line = line.replace(self.listOld[one], self.listNew[one])
			f2.write(line)
		f1.close()
		f2.close()
	def toTest(self, dirin, dirout):
		permission = pd.read_csv(dirin)
		listPer = permission[self.listNew]
		listPer.to_csv(dirout, index = False)
if __name__=="__main__":
	ad = sigpid()
	#ad.replace('F:\\document\\malgenome-215-dataset-1260malware-2539-benign_new.csv', 'F:\\document\\malgenome-215-dataset-1260malware-2539-benign_new_format.csv')
	ad.toTest('F:\\document\\sigpidBycckenny\\bjtuTrain.csv', 'F:\\document\\sigpidBycckenny\\bjtuTest.csv')