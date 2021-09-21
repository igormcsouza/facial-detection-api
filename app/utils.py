import base64

import cv2
import numpy


def base64_to_nparray(im_b64: str) -> numpy.ndarray:
    im_bytes = base64.b64decode(im_b64)
    im_arr = numpy.frombuffer(im_bytes, dtype=numpy.uint8)
    return cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
