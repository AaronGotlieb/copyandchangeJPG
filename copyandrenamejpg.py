import os
import shutil
import random

topdir = '' # directory with all pictures in directory or subdirectory
dest   = '' # destination of data to be copied

exten = '.jpg'
count = 0

def incrament():
	global count
	count = count + 1

def step(ext, dirname, names):
	ext = ext.lower()
	for name in names:
		if name.lower().endswith(ext):
			incrament()
			a = os.path.join(dirname, name)
			b = name
			c = a.replace(b,str(count)+'.JPG')
			print(b)
			os.rename(a,c)
			shutil.copy2(c,dest)

print('start')
os.path.walk(topdir, step, exten)
print('end')
