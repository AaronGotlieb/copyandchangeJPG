import os
import shutil

topdir = '' # source directory with all pictures in specific directory or subdirectory
dest   = '' # destination of data to be copied

exten = '.JPG' #change for different file type to be copied
count = 0      #global counter for renaming

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
			print(b)
			c = a.replace(b,str(count)+'.JPG') #also change file type here here 
			os.rename(a,c)
			shutil.copy2(c,dest)

print('start')
os.path.walk(topdir, step, exten)
print('Copied ', count, 'files with the final file named: ')
print('end')
