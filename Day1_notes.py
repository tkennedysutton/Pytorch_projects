# Day 1 training, firstly importing torch to play with it
import torch
# create a 1 dimensional tensor with values [1,2,3]
tensor_a = torch.tensor([1,2,3])
# print the tensor 
print("Tensor A:", tensor_a)
print("Shape of tensor_a:", tensor_a.shape)
# For a 1D tensor:
print("First element:", tensor_a[0])

# Create a 2D tensor (tensor is an object in python):
tensor_b = torch.tensor([[1, 2, 3], [4, 5, 6]])
print("Tensor B:", tensor_b)
print("Shape of tensor B", tensor_b.shape)
# Print specific element that will be found at row 0, column 1
print("Element at row 0, column 1",tensor_b[0,1])
