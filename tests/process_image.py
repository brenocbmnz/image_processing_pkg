from tkinter import Tk
from tkinter.filedialog import askopenfilename
from image_processing_pkg.filters import apply_blur, apply_sharpen
from image_processing_pkg.transformations import resize_image, rotate_image
from image_processing_pkg.utils import load_image, save_image

def select_image():
    """Abre uma janela de diálogo para selecionar uma imagem."""
    root = Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    filepath = askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    return filepath

def main():
    # Abre uma janela para o usuário escolher uma imagem
    image_path = select_image()

    # Carrega a imagem selecionada
    image = load_image(image_path)

    # Aplica um filtro de desfoque
    blurred_image = apply_blur(image, radius=5)

    # Aplica um filtro de nitidez
    sharpened_image = apply_sharpen(image)

    # Redimensiona a imagem
    resized_image = resize_image(image, (200, 200))

    # Rotaciona a imagem em 45 graus
    rotated_image = rotate_image(image, 45)

    # Salva as imagens processadas
    save_image(blurred_image, 'blurred_image.jpg')
    save_image(sharpened_image, 'sharpened_image.jpg')
    save_image(resized_image, 'resized_image.jpg')
    save_image(rotated_image, 'rotated_image.jpg')

if __name__ == "__main__":
    main()
