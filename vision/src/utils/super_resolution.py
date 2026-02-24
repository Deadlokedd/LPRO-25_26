import pathlib
from basicsr.archs.rrdbnet_arch import RRDBNet
from basicsr.utils.download_util import load_file_from_url
from realesrgan import RealESRGANer
from .. import config

_VISION_DIR = pathlib.Path(__file__).resolve().parent.parent.parent


def init_upscaler(model_name='RealESRGAN_x2plus', half=True, gpu_id=0):
    """Initialize Real-ESRGAN upscaler."""
    if model_name == 'RealESRGAN_x2plus':
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2)
        netscale = 2
    else:
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
        netscale = 4

    model_path = load_file_from_url(
        url=config.SR_MODEL_URLS[model_name],
        model_dir=str(_VISION_DIR / "models"),
        progress=True
    )

    sr_model = RealESRGANer(
        scale=netscale,
        model_path=model_path,
        model=model,
        tile=0,
        tile_pad=10,
        pre_pad=0,
        half=half,
        gpu_id=gpu_id
    )
    return sr_model


def upscale(img, sr_model, outscale=None):
    """Apply Real-ESRGAN super-resolution to an image."""
    if outscale is None:
        outscale = sr_model.scale
    output, _ = sr_model.enhance(img, outscale=outscale)
    return output
