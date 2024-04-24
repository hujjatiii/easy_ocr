import easyocr
from matplotlib import pyplot as plt
import cv2
import numpy as np 


IMAGE_PATH = "sample.png"

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)
result