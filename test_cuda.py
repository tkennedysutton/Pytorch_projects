import torch  # Make sure to import torch

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")  # Use the GPU
    tensor = torch.tensor([1.0, 2.0, 3.0])  # Create a tensor
    tensor_gpu = tensor.to(device)  # Move tensor to GPU
    print(f"Tensor on GPU: {tensor_gpu}")
else:
    print("CUDA not available.")
