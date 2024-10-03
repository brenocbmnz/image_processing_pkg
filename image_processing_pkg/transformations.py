from PIL import Image

def resize_image(image: Image, size: tuple) -> Image:
    """Redimensiona a imagem para o tamanho fornecido."""
    return image.resize(size)

def rotate_image(image: Image, angle: int) -> Image:
    """Roda a imagem em um determinado ângulo."""
    return image.rotate(angle)
