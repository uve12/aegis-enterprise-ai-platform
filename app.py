from fastapi import FastAPI


app = FastAPI(
    title="Aegis Enterprise AI Platform",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "0.1.0"
    }
