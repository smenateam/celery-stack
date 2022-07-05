from pydantic import BaseModel


class CreateTaskApiParameters(BaseModel):
    sleep_seconds: int
