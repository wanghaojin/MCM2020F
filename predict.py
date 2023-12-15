import torch 
import torch.nn as nn
from tqdm import tqdm

net = nn.ModuleList([nn.Linear(1, 16), nn.ReLU()])
for i in range(3):
    net.append(nn.Linear(4**(i+2),4**(i+3)))
    net.append(nn.Relu())
for i in range(3):
    net.append(nn.Linear(4**(5-i),4**(4-i)))
    net.append(nn.relu())
net.append(nn.Linear(16,1))
            