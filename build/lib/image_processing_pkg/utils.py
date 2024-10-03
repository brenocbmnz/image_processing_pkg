from PIL import Image

def load_image(filepath: str) -> Image:
    """Carrega uma imagem a partir de um arquivo."""
    return Image.open(filepath)

def save_image(image: Image, filepath: str) -> None:
    """Salva a imagem em um arquivo."""
    image.save(filepath)
