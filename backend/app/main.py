from fastapi import FastAPI

app = FastAPI(title="Yolo Object Detection API")

@app.get("/health")
def health_check():
	return{"status": "ok"}

@app.get("/")
def root():
	return{"message": "YOLO object Detection API is running"}
