#!/usr/bin/env python

# georeader.py -- Scrapes dataset URLs and other useful information from a GEO matrix.

import os
import sys
from ftplib import FTP


def main(args):
    if len(args)!=3:
        print len(args)
        print("Usage: %s matrixdir outfile" % args[0])
        return
    
    # List all of the files in the input directory:
    files=os.listdir(args[1])
    
    if len(files)==0:
        print("ERROR: Matrix dir contains no GEO matrices!")
        return
    
    urllist=[]
    title=""
    contrib=None
    date=None
    
    # Open the first file, if it exists, to scrape a useful project title:
    for fname in files:
        f=open(os.path.join(args[1], fname))
        lines=f.read().splitlines()
        
        for l in lines:
            toks=l.split('\t')
            if toks[0]=="!Series_contributor" and contrib is None:
                # Get the first contributor's last name:
                nametoks=toks[1].split(',')
                contrib=nametoks[2].strip('"')
            elif toks[0]=="!Series_submission_date" and date is None:
                datetoks=toks[1].split()
                date=datetoks[2].strip('"')
            elif toks[0]=="!Sample_supplementary_file_1":
                for u in toks[1:]:
                    urllist.append(u.strip('"'))
    
    title=contrib+date
    print("Project title: %s" % title)
    print("Url list:")
    print(urllist)
    finalurllist=[]
    
    # Now we need to determine where each sra file is in the path provided:
    for u in urllist:
        print("Exploring %s..." % u)
        urltoks=u.split('/')
        ftp=FTP(urltoks[2])
        ftp.login()
        rawpath=os.path.join(*urltoks[3:])
        ftp.cwd(rawpath)
        entries=ftp.nlst()
        
        for e in entries:
            realname=e
            print os.path.join(rawpath, realname)
            ftp.cwd("/"+os.path.join(rawpath, realname))
            newentry=ftp.nlst()
            
            finalurllist.append(os.path.join(u, realname, newentry[0]))
    print("Fixed URL list:")
    print(finalurllist)
    
    print("Writing %s/%s" % (args[1], args[2]))
    
    f=open(os.path.join(args[1], args[2]), 'w')
    f.write(title+"\n")
    
    for u in finalurllist:
        f.write("%s\n" % u)
    f.close()
    
if __name__=="__main__":
    main(sys.argv)