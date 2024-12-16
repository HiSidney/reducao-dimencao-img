import requests
from PIL import Image
from io import BytesIO

def rgb_to_gray(r, g, b):
    """Converte uma cor RGB para tons de cinza usando a fórmula de luminosidade."""
    gray = int(0.3 * r + 0.59 * g + 0.11 * b)
    return gray

def gray_to_bw(gray, threshold=128):
    """Converte uma imagem em tons de cinza para preto e branco com base em um limiar."""
    return 255 if gray >= threshold else 0

def process_image(image_url):
    """Processa a imagem colorida para tons de cinza e depois para preto e branco."""
    # Baixa a imagem da URL
    response = requests.get(image_url)
    
    # Abre a imagem usando PIL a partir da resposta da URL
    img = Image.open(BytesIO(response.content))
    
    # Converte a imagem para RGB (no caso de ela estar em outro formato)
    img = img.convert("RGB")
    
    # Obtém os pixels da imagem
    pixels = img.load()
    
    # Obtemos as dimensões da imagem
    width, height = img.size
    
    result = []
    for y in range(height):
        result_row = []
        for x in range(width):
            r, g, b = pixels[x, y]
            # Converte para cinza
            gray = rgb_to_gray(r, g, b)
            # Converte para preto e branco
            bw_pixel = gray_to_bw(gray)
            result_row.append(bw_pixel)
        result.append(result_row)
    
    return result

# Exemplo de URL de imagem
image_url = 'https://imgs.search.brave.com/_3XyM__kgyCZIgTsu4fTLMPFB28InmuEtT-clZ3u2Zw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9yc3py/LmdldGltZy5haS9y/ZXNpemU_dXJsPWh0/dHBzOi8vaW1nLmdl/dGltZy5haS9nZW5l/cmF0ZWQvaW1nLVE3/QmhTZGY4SHY3bUZP/eTlvZmxWSi5qcGVn/JnR5cGU9d2VicCZ3/aWR0aD0xMDgwJnNw/ZWVkPTU'

# Processa a imagem
imagem_processada = process_image(image_url)

# Exibe a imagem processada em preto e branco
for row in imagem_processada:
    print(row)