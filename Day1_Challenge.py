#This is a challeng to write a function that takes a list of numbers, converts the list to a pytorch tensor, reshapes it to a 2d tensor [2,-1] and returns the first row of this reshaped tensor
import torch
#The below is define the function to accept any list 
def process_list(input_list):
    tensor = torch.tensor(input_list)   #convert list to PyTorch tensor
    reshaped = tensor.view(3,-1)        #reshape to [2,-1] in PyTorch, -1 is a placeholder that tells PyTorch
    return reshaped [2]                 #returns first row - 0 means first row, 1 means second row
#The below is calling the function with my own list
my_list = [1,3,5,7,5,4,3,5,7,6,5,4,3,9,12,18,2,-1]
result = process_list(my_list)
print(result)

