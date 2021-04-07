#! /bin/env python

################################################################################
# Pairwise distance-based scoring function for prediction of ligand binding affinity
# Copyright 2019-2020 Lawrence Livermore National Security, LLC and American Heart Association
# Author: Fangqiang Zhu
# Last update: 2020/03/06
# 
# Please cite the following publication for reference of this code:
#   Binding Affinity Prediction by Pairwise Function Based on Neural Network
#   Fangqiang Zhu, Xiaohua Zhang, Jonathan E. Allen, Derek Jones, and Felice C. Lightstone
#   J. Chem. Inf. Model. 2020, 60, 2766-2772
################################################################################


import sys
import numpy
import torch


net = torch.nn.Sequential(
   torch.nn.Linear(7, 32),
   torch.nn.ReLU(),
   torch.nn.Linear(32, 32),
   torch.nn.ReLU(),
   torch.nn.Linear(32, 16),
   torch.nn.ReLU(),
   torch.nn.Linear(16, 8),
   torch.nn.ReLU(),
   torch.nn.Linear(8, 4),
   torch.nn.ReLU(),
   torch.nn.Linear(4, 2),
   torch.nn.ReLU(),
   torch.nn.Linear(2, 1),
)

device = torch.device('cpu')

net.load_state_dict(torch.load('net.pth', map_location = device))
net.eval()

X = numpy.load(sys.argv[1])

with torch.no_grad() :
   Y = net(torch.tensor(X))

print("log(Ka) = %.2f" % Y.sum())
