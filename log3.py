# _*_ coding:utf-8 _*_

import os
rootDir = '/Users/guohongke/runoob/recruitment/app/conf'

def fileFinder(rootDir):
    fileList = []
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            name, ext = os.path.splitext(filespath)
            if (ext == '.conf'):
                fileList.append(os.path.join(root,filespath))
    return fileList

lis = fileFinder(rootDir)

for i in lis:
    f = open(i,'r+')
    for line in f:
        f.write(line.replace('3306','3388'))
    f.close()

