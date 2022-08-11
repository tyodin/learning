import zipfile
import os
test = zipfile.ZipFile('test.ofd')
test.extractall()
test.close()
print ('解压完毕')