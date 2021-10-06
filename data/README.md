# The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions

Tschandl, Philipp, 2018, "The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions", https://doi.org/10.7910/DVN/DBW86T, Harvard Dataverse, V3, UNF:6:/APKSsDGVDhwPBWzsStU5A== [fileUNF]
___

Please download the repository from the link above and place it in your local ```skin-sweep-backend/data/ham10000``` folder:
* Extract both images to ```ham10000/images```
* Extract the segmentation data to ```ham1000/segmentation```

We are *not* committing the full 3GB+ database here for the sake of keeping the repo size reasonable.

Eventually we should cache the database(s) on an AWS server and make the neural net script only download it as necessary, or set up a git submodule dedicated to just storing the images. This way the front-end developers won't need to clutter their storage with the training set. 
