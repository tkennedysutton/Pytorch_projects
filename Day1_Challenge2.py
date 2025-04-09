def process_list(input_list):
    if len(input_list) % 2 !=0:
        raise ValueError("!!List length must be even to return [2,-1].")
    
    import torch
    tensor = torch.tensor(input_list, dtype=torch.float)
    reshaped = tensor.view(2,-1)
    return reshaped [0].unsqueeze(0), reshaped[1].unsqueeze(0)
my_list = [1,2,3,4,5,6,7,8,9,1,2,2]
result = process_list(my_list)
row1, row2 = result
print("first row", row1)
print("second row",row2)