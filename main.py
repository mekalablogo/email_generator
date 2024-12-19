from fastapi import FastAPI,Request
from routes import email_generator
from middleware import global_exception_handler
app = FastAPI()

@app.get("/health")
def health_check():
  return "Health is good"

# Global exception handling middleware
app.middleware("http")(global_exception_handler)  

app.include_router(email_generator)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)