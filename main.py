from fastapi import FastAPI 
app= FastAPI(title="Meeting Action Agent API")

@app.get("/health")
def health_check():
	return {"status": "ok"}
