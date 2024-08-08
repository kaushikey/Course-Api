from fastapi import FastAPI
from courses import courses_router
from upload import upload_router

app = FastAPI(
    summary="Api assignment",
    contact={
        "name": "Kaushikey Gupta",
        "email": "kaushikey945022@gmail.com"
    },
    docs_url=None
)

@app.get("/")
async def health():
    return {"message": "I am up!"}

app.include_router(courses_router, prefix="/api/courses")
app.include_router(upload_router, prefix="/api/upload")

