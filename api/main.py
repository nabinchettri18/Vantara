from fastapi import FastAPI

app = FastAPI(title="Vantara Customer Behavior Prediction API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
