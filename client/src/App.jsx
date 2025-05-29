import React, { useState } from "react";
import axios from "axios"

function App() {
  const [file, setFile] = useState(null);
  const [resultImage, setResultImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload-data/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      setResultImage(response.data.image);
    } catch (error) {
      console.error("Upload failed:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-100 via-purple-50 to-white flex flex-col items-center justify-center px-4">
      <h1 className="text-4xl font-bold text-gray-800 mb-8">
        📊 Coordinate Heatmap Plotter
      </h1>

      <div className="bg-white shadow-xl rounded-2xl p-8 w-full max-w-md">
        <input
          type="file"
          accept=".csv,.txt"
          onChange={handleFileChange}
          className="w-full mb-4 text-gray-700"
        />

        <button
          onClick={handleUpload}
          disabled={loading || !file}
          className={`w-full py-3 px-6 rounded-xl text-white font-semibold transition-all ${
            loading || !file
              ? "bg-gray-400 cursor-not-allowed"
              : "bg-indigo-600 hover:bg-indigo-700"
          }`}
        >
          {loading ? "Generating Plot..." : "Upload & Generate Plot"}
        </button>
      </div>

      {resultImage && (
        <div className="mt-10 w-full max-w-2xl text-center">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">
            🖼️ Generated Plot
          </h2>
          <img
            src={resultImage}
            alt="Result"
            className="w-full rounded-xl border shadow-md"
          />
        </div>
      )}
    </div>
  );
}

export default App;