#!/usr/bin/env python

import os
import sys

outpath="/scratch/Shares/dowell/pubgro/zz_not_human_or_mouse"

if len(sys.argv)!=2:
        print("Usage: %s inputfile" % sys.argv[0])
        exit(0)

print("Reading URL list file...")
f=open(sys.argv[1])
lines=f.read().splitlines()

# The first line in this file should be the dataset name.
realoutpath=os.path.join(outpath, lines[0])+'/'
print("Creating directory: %s" % realoutpath)
try:
        os.mkdir(realoutpath)
except:
        pass

for l in lines[1:]:
        os.system("wget -P %s %s" % (realoutpath, l)) 
