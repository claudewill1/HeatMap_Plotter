from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from .services import file_service, plot_service

router = APIRouter()

@router.post("/upload-data")
async def upload_data(file: UploadFile = File(...)):
    """
      Handle uploaded file.
      - Save file locally.
      - Call read_and_plot_data()
      - Return image path or base64 string.
    """
    try:
        # Save the uploaded file to disk using file_service
        file_path = await file_service.save_file(file)

        # Call read_and_plot_data() with the saved file path
        data = await plot_service.read_and_plot_data(file_path)
        # Return JSON response with image URL or base64 image
        return JSONResponse(content=data)
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})