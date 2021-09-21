from os import getenv
from typing import Dict, List

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from app.detection import DetectFace
from app.utils import base64_to_nparray


app = FastAPI(debug=True if getenv("ENVIRONMENT", "dev") == "dev" else False)


class Body(BaseModel):
    img: str


detect_face = DetectFace()


@app.post("/detect")
def detect(body: Body) -> Dict[str, List[List[int]]]:
    try:
        img = base64_to_nparray(body.img)
        gray = detect_face.bgr_to_gray(img)
        results = detect_face.detect(gray)
    except ValueError as e:
        raise HTTPException(400, detail="Error with body, %s, is img in base64?" % e)  # noqa: E501
    except Exception as e:
        raise HTTPException(500, detail="Internal Error, contact API adm!" % e)

    return {"detection": results}
