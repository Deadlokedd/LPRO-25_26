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

rm -rf "$VENV_DIR"
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip

if [ "$CPU_MODE" = true ]; then
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
fi
pip install -e .

# realesrgan depends on basicsr (without fix), so we need to overwrite it
# with basicsr-fixed that fixes the broken import of torchvision >= 0.18.
pip install --force-reinstall --no-deps "basicsr-fixed>=1.4"

echo ""
