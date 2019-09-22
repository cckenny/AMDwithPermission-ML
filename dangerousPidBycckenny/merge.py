
import pandas as pd
import os
Folder_Path = r'F:\\document\\sigpidBycckenny\\new'          #要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path =  r'F:\\document\\sigpidBycckenny'       #拼接后要保存的文件路径
SaveFile_Name = r'newtest.csv'              #合并后要保存的文件名
 
#修改当前工作目录
os.chdir(Folder_Path)
#将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()
 
#读取第一个CSV文件并包含表头
df = pd.read_csv(Folder_Path +'\\'+ file_list[0])   #编码默认UTF-8，若乱码自行更改
 
#将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,index=False)
 
#循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '\\'+ file_list[i])
    df.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,index=False, header=False, mode='a+')