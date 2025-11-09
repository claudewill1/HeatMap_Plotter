import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import uuid
import base64
from io import BytesIO

def read_data_file(file_path):
    """
    Read a data file containing x, y, and z values.
    Assumes no header and space or tab delimited

    Args:
        file_path (str): Path to the uploaded file.
    
    Returns:
        DataFrame: Pandas DataFrame with x, y, z columns.
    """
    try:
        data = pd.read_csv(file_path, delim_whitespace=True, header=None, names=['x', 'y', 'z'])
        return data
    except Exception as e:
        raise ValueError(f"Error reading data file: {e}")
    
    def generate_heatmap_plot(data):
        """
        Generate a 2D scatter plot with color mapping based on z values.

        Args:
            data (DataFrame): Pandas DataFrame with x, y, z columns.    
        Returns:
            str: Base64 encoded PNG image of the plot.
        """

        try:
            x = data['x'].values
            y = data['y'].values
            z = data['z'].values

            plt.figure(figsize=(8, 6))
            sc = plt.scatter(x, y, c=z, cmap='viridis', s=80, edgecolors='black')
            plt.colorbar(sc, label='Z Value')
            plt.xlabel('X Coordinate')
            plt.ylabel('Y Coordinate')
            plt.title('2D Scatter Plot with Heatmap Colors')
            plt.grid(True)

            # Save plot to a BytesIO stream
            buffer = BytesIO()
            plt.savefig(buffer, format ='png', bbox_inches='tight')
            plt.close()
            buffer.seek(0)

            # Encode the image to base64
            img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            buffer.close()

            return f"data:image/png;base64,{image_base64}"
        except Exception as e:
            raise RuntimeError(f"Failed to generate heatmap plot: {e}")
        
def save_uploaded_file(upload_file, upload_dir='server/static'):
    """
    Save an uploaded file to a temporary location.
    
    Args:
        upload_file (UploadFile): Uploaded file from FastAPI.
        upload_dir (str): DIrectory to save uploaded files.
    Returns:
        str: Path to the saved file.   
    """
    try:
        os.makedirs(upload_dir, exist_ok=True)
        file_ext = os.path.splitext(upload_file.filename)[1]
        file_name = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(upload_dir, file_name) 

        with open(file_path, "wb") as buffer:
            buffer.write(upload_file.file.read())
            
        return file_path
    except Exception as e:
        raise Runtime