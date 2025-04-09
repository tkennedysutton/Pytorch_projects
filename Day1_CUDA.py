import torch

def process_list(input_list):
    if len(input_list) % 2 != 0:
        raise ValueError("!!List length must be even to return [2,-1].")

    # Create the tensor from the list
    tensor = torch.tensor(input_list, dtype=torch.float)

    # Check if CUDA is available and move the tensor to the GPU if possible
    if torch.cuda.is_available():
        device = torch.device("cuda")  # Set device to GPU
        tensor = tensor.to(device)  # Move tensor to GPU

    # Reshape the tensor to 2 rows, with the number of columns inferred
    reshaped = tensor.view(2, -1)

    # Return the rows as separate tensors with an additional unsqueeze (to make them 2D tensors)
    return reshaped[0].unsqueeze(0), reshaped[1].unsqueeze(0)

# Example list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 2]

# Process the list
result = process_list(my_list)

# Unpack the rows
row1, row2 = result

# Print the rows
print("First row:", row1)
print("Second row:", row2)

# Check if tensors are on the GPU
print("Row 1 device:", row1.device)
print("Row 2 device:", row2.device)
