import uvicorn
import settings

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=settings.LISTEN_PORT, log_level=settings.LOG_LEVEL)
