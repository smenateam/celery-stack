import models
import tasks
from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.post("/tasks/create")
async def create_task(params: models.CreateTaskApiParameters):
    task = tasks.sleeper_task.delay(params.sleep_seconds)

    return {
        "task": {
            "id": task.id,
        },
        "message": "Task was created",
    }
