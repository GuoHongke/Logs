# _*_ coding:utf-8 _*_

import os

aimID = '2701823d-652a-35ab-9963-897360e98086'
rootDir = '/Users/guohongke/runoob/recruitment/app/logs/bdp-di'

def fileFinder(rootDir):
    fileList = []
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            name, ext = os.path.splitext(filespath)
            fileList.append(os.path.join(root,filespath))
    return fileList

lis = fileFinder(rootDir)

for i in lis:
    f = open(i,'r')
    for line in f:
        if(aimID in line):
            print line.split()[6],line.split()[7]
    f.close()








