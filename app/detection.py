from typing import Any, List, Tuple

import cv2
import numpy


class DetectFace:

    detector = cv2.CascadeClassifier("models/haarcascade_frontalface_alt.xml")

    def __init__(self,
                 scaleFactor: float = 1.05,
                 minNeighbors: int = 5,
                 minSize: Tuple[int, int] = (30, 30),
                 flags: Any = cv2.CASCADE_SCALE_IMAGE):
        self.scaleFactor = scaleFactor
        self.minNeighbors = minNeighbors
        self.minSize = minSize
        self.flags = flags

    def bgr_to_gray(self, img: numpy.ndarray) -> numpy.ndarray:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def detect(self, img: numpy.ndarray) -> List[List[int]]:
        """Run detection on a given image."""
        results = self.detector\
            .detectMultiScale(img,
                              scaleFactor=self.scaleFactor,
                              minNeighbors=self.minNeighbors,
                              minSize=self.minSize,
                              flags=self.flags)

        return results.tolist()
