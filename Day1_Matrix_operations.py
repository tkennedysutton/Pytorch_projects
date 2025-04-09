import torch

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")  # Use the GPU
    # Create tensors A and B on the CPU
    A = torch.rand(500, 5000,device="cuda")
    B = torch.rand(500, 5000, device="cuda")

    # Perform element-wise multiplication on GPU
    add_result = A * B  # Element-wise multiplication
    print("Multiplication result on GPU:", add_result)
else:
    print("CUDA is not available, staying on CPU")
