from PIL import Image, ImageFilter

def apply_blur(image: Image, radius: int = 2) -> Image:
    """Aplica um filtro de desfoque (blur) na imagem."""
    return image.filter(ImageFilter.GaussianBlur(radius))

def apply_sharpen(image: Image) -> Image:
    """Aplica um filtro de nitidez (sharpen) na imagem."""
    return image.filter(ImageFilter.SHARPEN)
