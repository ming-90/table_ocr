import cv2
import numpy as np
from fastapi import UploadFile


async def convert_image(file: UploadFile) -> np.ndarray:
    """Convert image to numpy array."""
    image = await file.read()
    image_bytes = np.frombuffer(image, dtype=np.uint8)
    image_decoded = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    image_gray = cv2.cvtColor(image_decoded, cv2.COLOR_BGR2GRAY)
    return image_gray
