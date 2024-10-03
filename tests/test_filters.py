import unittest
from PIL import Image  # Importa a classe Image
from image_processing_pkg.filters import apply_blur, apply_sharpen

class TestFilters(unittest.TestCase):
    def setUp(self):
        # Cria uma imagem simples de teste
        self.image = Image.new('RGB', (100, 100), color='red')

    def test_apply_blur(self):
        blurred_image = apply_blur(self.image)
        self.assertIsInstance(blurred_image, Image.Image)  # Use Image.Image para verificar a instância

    def test_apply_sharpen(self):
        sharpened_image = apply_sharpen(self.image)
        self.assertIsInstance(sharpened_image, Image.Image)  # Use Image.Image para verificar a instância

if __name__ == '__main__':
    unittest.main()
