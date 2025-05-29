// Import React and necessary hooks
import React, { useState } from 'react';
import axios from 'axios';
// Create a FileUpload component
const FileUpload = ({ onUploadSuccess }) => {
    // State to track selected file
    const [file, setFile] = useState(null);
    // State to track upload status
    const [uploading, setUploading] = useState(false);
    // State to track error message
    const [error, setError] = useState('');
    // Function to handle file selection
    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
        setError(''); // Reset error message on new file selection
    }
    // Handle form submission (file upload)
    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!file) {
            setError('Please select a file to upload.');
            return;
        }
        setUploading(true);
        setError('');
        const formData = new FormData();
        formData.append('file', file);
        try {
            // Make POST request to upload the file
            const response = await axios.post('http://127.0.0.1:8000/upload-data/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            // Call the onUploadSuccess callback with the response data
            onUploadSuccess(response.data);

            // Reset the state after successful upload
            setSelectedFile(null);
            setUploading(false);
            setError('');
        } catch (err) {
            console.error(err);
            // Handle error during file upload
            setError('File upload failed. Check server connection.');
        } finally {
            setUploading(false);
        }   
        
    };

    return (
        <div className="p-4 bg-white rounded-xl shadow w-full max-w-md mx-auto">
            <h2 className="text-xl font-semibold mb-4">Upload Data File</h2>

            {/* File input */}
            <input type="file" onChange={handleFileChange} className="mb-4" accept=".csv, .txt, .xlsx" />

            {/* Upload button */}
            <button
                onClick={handleUpload}
                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
                disabled={uploading || !file}
            >
                {uploading ? 'Uploading...' : 'Upload File'}  
            </button>
            {/* Error message */}
            {error && <p className="text-red-500 mt-3">{error}</p>}
</div>
    );
};

export default FileUpload;
