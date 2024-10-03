from setuptools import setup, find_packages

setup(
    name='image_processing_pkg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Biblioteca para manipulação de imagens
        # Adicione outras bibliotecas necessárias
    ],
    description='A simple image processing package',
    author='Seu Nome',
    author_email='seuemail@exemplo.com',
    url='https://github.com/seuperfil/image_processing_pkg',
)
