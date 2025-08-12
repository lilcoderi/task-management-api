# Task Management API

A **FastAPI** backend service for managing tasks with categories, priorities, and deadlines. It implements clean architecture principles, proper error handling, filtering, and sorting capabilities.

---


| **Live API (Vercel)** | **Swagger Docs (Vercel)** |
| :------------------------------------------------ | :--------------------------------------------------- |
| [https://task-management-api-1fmu.vercel.app](https://task-management-api-1fmu.vercel.app) | [https://task-management-api-1fmu.vercel.app/docs](https://task-management-api-1fmu.vercel.app/docs) |

| **Live API** | **Swagger Docs** |
| :------------------------------------------------ | :--------------------------------------------------- |
| [https://taskmanagementapi.up.railway.app](https://taskmanagementapi.up.railway.app) | [https://taskmanagementapi.up.railway.app/docs](https://taskmanagementapi.up.railway.app/docs) |

---

## Features

* **CRUD Tasks** – Create, Read, Update, and Delete tasks with ease.
* **Categories & Priorities** – Assign any category and priority (`Low`, `Medium`, `High`) to your tasks.
* **Deadline Tracking** – Validate and monitor task deadlines to keep track of your progress.
* **Filtering & Sorting**
    * Filter tasks by `category`, `priority`, or a date range (`deadline_from`, `deadline_to`).
    * Sort results by `created_at`, `priority`, or `deadline` in `asc` (ascending) or `desc` (descending) order.
* **Validation** – Ensures non-empty titles, valid deadline formats, and correct priority values.
* **Error Handling** – Returns clear HTTP status codes and descriptive error messages for better API consumption.
* **Interactive Docs** – Auto-generated Swagger UI available at `/docs` for easy API exploration and testing.

---

## Tech Stack

| Layer           | Technology                           |
| :-------------- | :----------------------------------- |
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Database** | MySQL                                |
| **ORM** | SQLAlchemy                           |
| **Deployment** | [Railway](https://railway.app/)      |
| **Documentation** | Swagger                |

---

## Database Schema

The database schema defines the structure of the `tasks` table:

```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(100),
    priority ENUM('Low', 'Medium', 'High') NOT NULL,
    deadline DATETIME NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

---

## Running the Project Locally

Follow these steps to set up and run the project in your local environment.

**1. Clone Repository**
```bash
git clone https://github.com/lilcoderi/task-management-api.git
cd task-management-api
```

**2. Create Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

**3. Setup Environment Variables**

Create a .env file in the root directory:

```bash
DB_HOST=your_database_host
DB_PORT=your_database_port
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```

**4. Run the Server**
```bash
uvicorn app.main:app --reload
```
API will be available at:
* Local: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs

---

## API Endpoints

**POST /tasks**
***– Create a new task.***

Request Body:
```json
    {
        "title": "Complete Assignment",
        "description": "Finish the backend API",
        "category": "Work",
        "priority": "High",
        "deadline": "2025-08-15T23:59:59"
    }
```

**GET /tasks**
***– Retrieve all tasks (with optional filters).***

Example Filters:
```bash
GET /tasks?category=Work&priority=High
GET /tasks?deadline_from=2025-08-01T00:00:00&deadline_to=2025-08-31T23:59:59
GET /tasks?sort_by=deadline&sort_order=desc
```

**GET /tasks/{id}**
***– Retrieve a specific task by its ID.***

**PUT /tasks/{id}**
***– Update a task's details.***

**DELETE /tasks/{id}**
***– Delete a task by its ID.***

---

## Testing

Run unit tests to ensure all business logic works as expected:
```bash
pytest
```

---

## Deployment Details

This API is deployed on Railway.

| **Base URL** | **Swagger URL** |
| :------------------------------------------------ | :--------------------------------------------------- |
| [https://taskmanagementapi.up.railway.app](https://taskmanagementapi.up.railway.app) | [https://taskmanagementapi.up.railway.app/docs](https://taskmanagementapi.up.railway.app/docs) |

Start Command (Procfile):
```bash
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## Design Decisions

* FastAPI + SQLAlchemy for performance and ORM convenience.
* Pydantic for request validation and serialization.
* Layered Architecture: Separate concerns into models, schemas, CRUD, and routes.
* Environment Variables for secure configuration.
* Swagger UI for API documentation.

---

## Author

Developed by Riana Nur Anisa as part of a software engineering test project.