
# Project Name

This project is a FastAPI application that requires the installation of specific Python packages. Follow the instructions below to set up and run the project in a development environment.

## Requirements

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- Enum package

## Installation

1. **Clone the repository** (if needed).

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Install dependencies**

   - Install `FastAPI` with the standard dependencies:
     ```bash
     pip install "fastapi[standard]"
     ```

   - Install `enum`:
     ```bash
     pip install enum
     ```

## Running the Application

To start the FastAPI server in development mode, run:

```bash
uvicorn main:app --reload
```

Replace `main` with the name of your Python file (e.g., `main.py` if that's the file containing the FastAPI app).

## Development

For development, use the following command:

```bash
fastapi dev main.py
```

This command will start the FastAPI app with live reloading enabled, making it easier to test changes on the fly.

## Usage

Once the server is running, you can access the interactive API documentation by visiting:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
