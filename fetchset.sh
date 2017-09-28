#!/bin/bash

# This script automatically fetches all data in a geo matrix URL
# and dumps it into /scratch/Shares/dowell/pubgro/zz_not_human_or_mouse/<the appropriate paper name>

georeader="/Users/migo0123/georeader.py"
dnldset="/Users/migo0123/dnldset.py"

echo $#
if [ $# != 2 ]; then
        echo "Fetches an entire dataset based on a GEO series matrix URL"
        echo "Usage: $0 inputurl workdir"
        echo "Example: ./fetchset.sh ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE68nnn/GSE68677/matrix/ tmp"
        exit 1
fi

mkdir $2
cd $2
wget -r -nH -nd -np -R index.html* $1
gzip -d *
cd ..
$georeader $2 out.txt
echo "PAPER NAME: `head -n 1 $2/out.txt`"

$dnldset $2/out.txt 
