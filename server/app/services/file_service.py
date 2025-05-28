import os

def save_uploaded_file(uploade_file, destination_dir="uploads"):
    """
       Save the uploaded file to destination directory.
       - Ensure directory exists.
       - Write file contents to disk.
       - Return the saved file path.
    """

    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    # Create a full path for saving the file
    file_path = os.path.join(destination_dir, uploade_file.filename)
    # Open destination file in write-binary mode
    with open(file_path, "wb") as buffer:
        # Write the contents of the uploaded file to the destination file
        buffer.write(uploade_file.file.read())
    # Return the path where the file was saved
    return file_path

    
