
import os
import sys
import pdb

def search_file(path, x = '.'):
	for obj in os.listdir(path):
		childpath = os.path.join(path, obj)
		if os.path.isfile(childpath):
			# pdb.set_trace()
			if x in os.path.splitext(obj)[0]:
				print childpath
		else:
			# pdb.set_trace()
            
			search_file(childpath, x)

l = sys.argv
if len(l) == 2:
	search_file('.', l[1])
else:
	print('error')