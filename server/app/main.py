from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import routes
import uvicorn

app = FastAPI()

# Allow fronend app to interact with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, adjust as needed
    allow_headers=["*"],  # Allows all headers, adjust as needed
)
# Include the routes from the routes module
app.include_router(routes.router) 

if __name__ == "__main__":
    # Run the FastAPI app with Uvicorn on localhost:8000
    unvicorn.run("app, host='127.0.0.1", port=8000, reload=True)