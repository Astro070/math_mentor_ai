# utils/ocr.py
import easyocr, numpy as np
from PIL import Image

reader = easyocr.Reader(['en'])

def extract_text_from_image(file):
    img = np.array(Image.open(file))
    result = reader.readtext(img)   # list of (bbox, text, conf)
    texts = [r[1] for r in result]
    confs = [r[2] for r in result]
    avg_conf = float(np.mean(confs)) if confs else 0.0
    return " ".join(texts), avg_conf