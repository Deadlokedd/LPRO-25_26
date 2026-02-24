"""Available hardware information (GPU/VRAM)."""
import torch

def vram_usage(label=""):
    """Show VRAM used at that moment."""
    if torch.cuda.is_available():
        used = torch.cuda.memory_allocated(0) / 1e9
        reserved = torch.cuda.memory_reserved(0) / 1e9
        total = torch.cuda.get_device_properties(0).total_memory / 1e9
        print(f"[VRAM {label}] Used: {used:.2f} GB | Reserved: {reserved:.2f} GB | Total: {total:.2f} GB")
