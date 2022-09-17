from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from server.controllers.graphology_controler import Output
from server.utils.save_file import save_file
from server.utils.train_predict import graphology_prediction

router = APIRouter(prefix="/services")


@router.post("/graphology")
def grapohology_analysis(file: UploadFile = File(None)):
    try:
        file_name=save_file(file=file)
        prediction= graphology_prediction(file_name=file_name)
        if prediction is None:
            return JSONResponse(
                status_code=200,
                content={
                    "success": False,
                    "data": None,
                    "message": "Data not available regarding image",
                    "error": None,
                },
            )
        else:
            return JSONResponse(
                status_code=200,
                content={
                    "success": True,
                    "data": prediction,
                    "message": "Analysis of Handwritten Image",
                    "error": None,
                },
            )
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "data": None,
                "message": "Something went wrong",
                "error": str(e),
            },
        )