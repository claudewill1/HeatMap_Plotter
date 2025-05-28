📊 Heatmap Plotting Web Application
📑 Overview

This is a full-stack web application that allows users to upload coordinate data files and visualize the data as a 2D scatter plot with color mapping based on a third variable (z-value). The system uses:

    Python (FastAPI) for the backend API server

    Matplotlib for data visualization

    React (with Vite) for the frontend user interface

The application reads a file containing a table of x, y, and z values and generates a color-coded 2D scatter plot where the z-values are represented by a color spectrum.
🎯 Purpose

This application was designed to provide an easy, interactive way for users to:

    Upload files containing 2D coordinate data with associated magnitude values.

    Automatically generate a visual plot of the data with color representing the third variable (z).

    Quickly interpret spatial patterns and trends in tabular data.

It is particularly useful for:

    Scientific data visualization

    Engineering simulation result analysis

    Surveying or mapping data plotting

⚙️ How It Works

    User Uploads Data File
    Through the frontend interface, the user uploads a .txt or .csv file containing x, y, z data columns.

    Data Processing
    The Python backend receives the file, reads the table, and extracts the data values.

    Plot Generation
    The backend uses Matplotlib to generate a 2D scatter plot where:

        X and Y define the position.

        Z is mapped to a color scale (Viridis colormap).

        A color bar is included for reference.

    Result Display
    The generated plot is converted to a base64-encoded image and returned to the frontend, where it is displayed immediately within the app interface.

📂 Project Structure

heatmap-app/
├── server/
│   ├── main.py                # FastAPI server entrypoint
│   ├── plotting.py            # Data parsing + plotting logic
│   ├── static/                # Generated plot images
│   └── requirements.txt       # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # React frontend component
│   │   └── main.jsx           # React entrypoint
│   ├── public/
│   └── package.json
│
└── README.md

📥 File Format Example

The data file should contain space or tab-separated values in the following format:

x y z
1 0.5 10
2 0.7 12
3 1.2 16
4 0.9 13
5 1.5 18

    x: X-coordinate

    y: Y-coordinate

    z: Value to be represented by color

🛠️ Installation & Running
📦 Backend (Python FastAPI)

cd server
pip install -r requirements.txt
uvicorn main:app --reload

🌐 Frontend (React + Vite)

cd frontend
npm install
npm run dev

📈 Dependencies
Backend:

    FastAPI

    Uvicorn

    Matplotlib

    Numpy

    Pandas

    python-multipart

Frontend:

    React

    Axios

    Vite

    Tailwind CSS

📊 Result Example

When a file is uploaded, the user will see a plot like this:

    2D scatter plot

    Points colored by z-value using a Viridis colormap

    Color bar legend

    Axis labels and grid lines

📣 Notes

    The application expects space- or tab-delimited text files.

    The plot image is dynamically generated and displayed without page reload.

    Colormap, point size, and appearance can be customized within plotting.py.

📌 Future Enhancements (Ideas)

    Add support for CSV headers.

    Add multiple colormap options.

    Enable image download.

    Dockerized deployment.

📃 License

This project is open-source and free to use for educational and research purposes.
📸 Interface Preview (Text Concept)

+----------------------------------------+
| 📊 Coordinate Heatmap Plotter          |
|                                        |
| [ Choose File ]                        |
|                                        |
| [ Upload & Generate Plot ]             |
|                                        |
| (After upload...)                      |
| 📸 Generated Plot                      |
|  [image displayed here]                |
+----------------------------------------+