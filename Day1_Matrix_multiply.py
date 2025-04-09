import torch
device = torch.device("cuda")
A = torch.rand(3,4,device="cuda")
B = torch.rand(4,5,device="cuda")
C=A @ B
print("Matrix multiplication",C.cpu())