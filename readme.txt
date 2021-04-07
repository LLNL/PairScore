This is a preliminary code to predict binding affinity from the pairwise
distances between protein and ligand atoms. Please cite the following
publication for reference of this code:

Binding Affinity Prediction by Pairwise Function Based on Neural Network
Fangqiang Zhu, Xiaohua Zhang, Jonathan E. Allen, Derek Jones, and Felice C. Lightstone
J. Chem. Inf. Model. 2020, 60, 2766-2772


The files in this folder are:
readme.txt - This file
calcPK.py - The python code to run the calculation
net.pth - The parameters for the trained neural network;
          needs to be in the same directory as calcPK.py
4llx.npy - An example of the input file for pose 4llx in PDBBind 2018

An example for running the code:
$ ./calcPK.py 4llx.npy 
log(Ka) = 3.86

The argument for calcPK.py is a numpy file for an array with 7 columns. Each
row represents a pair of atoms, one from the protein and one from the ligand.
Columns 1-3 are the charge, sigma, and epsilon for the protein atom.
Columns 4-6 are the charge, sigma, and epsilon for the ligand atom.
Column 7 is the distance (in Anstrom) between the two atoms.
See 4llx.npy as an example for this file.

Numpy and PyTorch are required to run this code.
