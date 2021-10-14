import os

cmd = 'adb devices'

# Using os.system() method
# os.system(cmd)

b= os.popen(cmd,'r',1)
print(b)
