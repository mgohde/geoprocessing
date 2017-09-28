This repo contains scripts that are useful in fetching datasets from NIH's GEO.

dnldset.py -- Downloads URLs listed in a file and places them in the directory specified in the first line of that file.

fetchset.sh -- Automatically downloads an entire GEO project given a series matrix directory URL. For example: ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE68nnn/GSE68677/matrix/

georeader.py -- Parses through a set of GEO series matrix files and generates a URL list file usable by the dnldset.py script.
