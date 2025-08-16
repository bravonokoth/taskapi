from fastapi import FastAPI, HTTPException
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import List

# Environment-based configuration
class Settings(BaseSettings):
    app_port: int = 8001

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

# Initialize FastAPI app with ORJSONResponse
app = FastAPI(default_response_class=ORJSONResponse)

# Pydantic model for Task
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# In-memory storage for tasks
tasks = []

# Endpoint to create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    for existing_task in tasks:
        if existing_task.id == task.id:
            raise HTTPException(status_code=400, detail="Task with this ID already exists")
    tasks.append(task)
    return task

# Endpoint to read all tasks
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

# Endpoint to read a single task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint to update a task by ID
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint to delete a task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

# Run the app with port from settings
if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run(app, host="0.0.0.0", port=settings.app_port)
    except OSError as e:
        print(f"Port {settings.app_port} in use: {e}. Try a different port, e.g., {settings.app_port + 1}.")