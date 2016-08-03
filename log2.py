# _*_ coding:utf-8 _*_

import os
import re

aimURL = '/api/warn/amount'
rootDir = '/Users/guohongke/runoob/recruitment/app/logs'


def fileFinder(rootDir):
    fileList = []
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            name, ext = os.path.splitext(filespath)
            fileList.append(os.path.join(root,filespath))
    return fileList

lis = fileFinder(rootDir)

count = 0
for i in lis:
    f = open(i,'r')
    nf = open('newLog.conf', 'w')
    for line in f:
        if aimURL in line:
            count += 1
        s = re.search(r'18:\d{2}:\d{2}', line)
        if str(s) == 'None':
            nf.write(line)
    f.close()
    nf.close()
print count