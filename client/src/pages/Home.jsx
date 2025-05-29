import React, { useState } from 'react';
import axios from 'axios';
import ImageDisplay from '../components/ImageDisplay';

/*
    * Home component
    * -Upload a file containing coordinate 
    * - Send the file to the backend API for processing
    * - Display the generated heatmap image once it's returned   * The main page of the HeatMap Plotter application.
    * Allows users to upload a data file and view the generated heatmap image.
    *
*/
function Home() {
    // State to store the selected file
    const [file, setFile] = useState(null);

    // State to store the returned image (base64 string)
    const [resultImage, setResultImage] = useState(null);

    // State to track if the app is currently uploading/processing
    const [loading, setLoading] = useState(false);

    /**
     * Handle file selection event
     * @param {Event} event - The file input change event
     */
    const handleFileChange = (event) => {
        setFile(event.target.files[0]); // Set the selected file
    }

    /**
     * handle file upload and plot generation.
     * Sends file to backendAPI and retrieves base64 image string.
     */
    const handleUpload = async () =>{
        if (!file) return; // If no file is selected, do nothing

        const formData = new FormData();
        formData.append("file", file); // Append the file to the form data
        setLoading(true); // Set loading state to true

        try {
            // Send POST request to backend API
            const response = await axios.post(
                "http://127.0.0.1:8000/upload-data/",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data", // Set content type for file upload
                    },
                }
            );

            // Save the returned bas64 image string to state.
            setResultImage(response.data.image);
        } catch (error) {
            console.error("Upload failed:", error); // Log any errors during upload
        } finally {
            setLoading(false); // Reset loading state
        }
    };

    return (
        <div className='min-h-screen bg-gradient-to-br from-indigo-100 via-purple-50 to-white flex flex-col items-center justify-center px-4'>
            {/* App heading */}
            <h1 className='text-4xl font-bold text-gray-800 mb-8'>
                📊 Coordinate Heatmap Plotter
            </h1>

            {/* Upload form container */}

            <div className='bg-white shadow-xl rounded-2xl p-8 w-full max-w-md'>
                <input
                    type="file"
                    accept=".csv,.txt" // Accept only CSV or TXT files
                    onChange={handleFileChange} // Handle file selection
                    className='w-full mb-4 text-gray-700'
                />
        <button
            onClick={handleUpload} // Handle upload button click
            disabled={loading || !file} // Disable if loading or no file selected
            className={`w-full py-3 px-6 rounded-xl text-white font-semibold transition-all ${
                loading || !file
                    ? "bg-gray-400 cursor-not-allowed"
                    : "bg-indigo-600 hover:bg-indigo-700"
            }`}     
        >
            {loading ? "Generating Plot..." : "Upload & Generate Plot"}
        </button>
    </div>

      {/* Display the image if one is returned */}
      <ImageDisplay imageSrc={resultImage} title="🖼️ Generated Plot" />
    </div>
  );
}