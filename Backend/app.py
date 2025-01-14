from flask import Flask, request, jsonify
from controllers.plot_controller import generate_heatmap
from flask_cors import CORS
import os

# Initialize Flask application
app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing to allow frontend requests



@app.route('/plot', methods=['POST'])
def plot_heatmap():
    # Endpoint to generate a heatmap based upon uploaded files
    return generate_heatmap(request)

@app.route('/static/<path:filename>')
def serve_static_file(filename):
    # Serve static files such as the generated heatmap image
    return app.send_static_file(filename)

if __name__ == '__main__':
    # Ensure the static directory exists before running the server
    os.makedirs('views/static', exist_ok=True)
    app.run(debug=True)
    
