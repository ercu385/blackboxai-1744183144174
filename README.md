
Built by https://www.blackbox.ai

---

```markdown
# Dijital Tarım API

## Project Overview
Dijital Tarım API is a FastAPI-based application designed for the Digital Agriculture solution integrated with SAP. It provides various endpoints to manage agricultural data, allowing users to access field information, weather data for specific fields, and interact with SAP for materials and production orders. The application is designed to be extensible and robust, featuring JWT authentication and an integration layer for SAP.

## Installation
To set up this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/digital_tarim_api.git
   cd digital_tarim_api
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   Make sure you have `pip` updated and then install FastAPI and other dependencies.
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**
   Create a file named `.env` in the root directory of the project and add any necessary environment variables as required for your setup.

5. **Run the application:**
   ```bash
   uvicorn app:app --reload
   ```

## Usage
Once the application is running, you can access the API at `http://127.0.0.1:8000`. The following endpoints are available:

- **GET /**: Returns the welcome message.
- **GET /api/fields**: Retrieves information about all fields (authentication required).
- **GET /api/weather/{field_id}**: Retrieves weather information for a specific field (authentication required).
- **GET /api/sap/materials**: Retrieves materials from SAP (authentication required).
- **POST /api/sap/create_order**: Creates a production order in SAP (authentication required).

Remember to provide a valid JWT token in the Authorization header for the endpoints that require authentication.

## Features
- Integration with SAP for fetching materials and creating production orders.
- JWT authentication for secure access to API endpoints.
- CORS middleware configured for mobile accessibility.
- Async database operations for better performance and scalability.
- Well-structured model definitions for farmers, fields, crops, and irrigations.

## Dependencies
The project has the following dependencies listed in `requirements.txt`:
- `fastapi`
- `uvicorn`
- `sqlalchemy`
- `asyncpg` (or other database drivers as necessary)
- `python-dotenv`
- `pydantic`

## Project Structure
```
/digital_tarim_api
│
├── app.py                  # Main FastAPI application setup
├── app_backup.py           # Backup of the application
├── database.py             # Database connection and ORM logic
├── models.py               # SQLAlchemy ORM models
├── sap_integration.py      # SAP integration layer (mock implementation)
├── static/                 # Directory for static files
├── templates/              # Directory for Jinja2 templates
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables configuration
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
```