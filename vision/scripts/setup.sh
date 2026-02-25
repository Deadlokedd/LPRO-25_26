#!/usr/bin/env bash
# scripts/setup.sh — Setup the environment.
#
# Usage:
#   cd vision/
#   bash scripts/setup.sh         # Install standard/GPU PyTorch
#   bash scripts/setup.sh --cpu   # Install CPU-only PyTorch
set -euo pipefail

VENV_DIR=".venv"
CPU_MODE=false

if [[ "${1:-}" == "--cpu" ]]; then
    CPU_MODE=true
fi

# Setup Python 3.11
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.11 python3.11-venv -y

rm -rf "$VENV_DIR"
python3.11 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

pip install --upgrade pip wheel
if [ "$CPU_MODE" = true ]; then
    pip install torch==2.1.0 torchvision==0.16.0 --index-url https://download.pytorch.org/whl/cpu
    pip install mmcv==2.1.0 -f https://download.openmmlab.com/mmcv/dist/cpu/torch2.1.0/index.html
else
    pip install torch==2.1.0 torchvision==0.16.0 --index-url https://download.pytorch.org/whl/cu121
    pip install mmcv==2.1.0 -f https://download.openmmlab.com/mmcv/dist/cu121/torch2.1.0/index.html
fi
pip install chumpy==0.70 --no-build-isolation
pip install -e .
# realesrgan depends on basicsr (without fix), so we need to overwrite it
# with basicsr-fixed that fixes the broken import of torchvision >= 0.18.
pip install --force-reinstall --no-deps "basicsr-fixed>=1.4"
# ensure numpy < 2.0.0 after everything is installed to avoid breaking compiled extensions
pip install "numpy<2.0.0" --force-reinstall --no-deps

echo ""
