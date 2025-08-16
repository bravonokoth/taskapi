# Task API  

A simple task management API built with [FastAPI](https://fastapi.tiangolo.com/).  
This project allows users to create, read, update, and delete tasks, with configuration managed via environment variables.  

## Features
- Create a new task with an ID, title, description, and completion status.  
- Retrieve a list of all tasks or a specific task by ID.  
- Update an existing task.  
- Delete a task by ID.  
- Uses `ORJSONResponse` for faster JSON serialization.  
- Environment-based configuration with `pydantic-settings`.  

## Prerequisites
- Python 3.12+  
- Git  
- A virtual environment (recommended)  
- A GitHub account with SSH key configured (for repository access)  

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine using SSH:

```bash
git clone git@github.com:bravonokoth/taskapi.git
cd taskapi
````

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn pydantic pydantic-settings orjson fastapi-cli
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and specify the port (default is 8000):

```bash
echo "APP_PORT=8001" > .env
```

### 5. Run the Application

Start the FastAPI development server:

```bash
fastapi dev main.py --port 8001
```

Or use Uvicorn directly:

```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

The API will be available at [http://localhost:8001](http://localhost:8001).

### 6. Access the Interactive API Docs

Open your browser and navigate to:

* [http://localhost:8001/docs](http://localhost:8001/docs) for Swagger UI
* [http://localhost:8001/redoc](http://localhost:8001/redoc) for ReDoc

---

## API Endpoints

| Method | Endpoint      | Description           |
| ------ | ------------- | --------------------- |
| POST   | `/tasks/`     | Create a new task     |
| GET    | `/tasks/`     | Retrieve all tasks    |
| GET    | `/tasks/{id}` | Retrieve a task by ID |
| PUT    | `/tasks/{id}` | Update a task by ID   |
| DELETE | `/tasks/{id}` | Delete a task by ID   |

---

## Example Request (Create a Task)

```bash
curl -X POST "http://localhost:8001/tasks/" \
-H "Content-Type: application/json" \
-d '{"id": 1, "title": "Sample Task", "description": "This is a sample task", "completed": false}'
```

## Example Response

```json
{
  "id": 1,
  "title": "Sample Task",
  "description": "This is a sample task",
  "completed": false
}
```

---

## Project Structure

```
taskapi/
├── main.py           # FastAPI application code
├── .env              # Environment variables (not tracked)
├── .gitignore        # Git ignore file
├── README.md         # This file
├── venv/             # Virtual environment (not tracked)
```




