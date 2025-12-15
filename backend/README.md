# Financial Management Backend

A minimal Flask backend API for the financial management application.

## Setup

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Running the Application

### Development Mode
```bash
poetry run python app.py
```

The server will start on `http://localhost:5000`

### Production Mode (with Gunicorn)
```bash
poetry run gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Endpoints

- `GET /` - Health check endpoint
- `GET /api/health` - API health check endpoint

## Project Structure

```
backend/
├── app.py          # Main Flask application
├── pyproject.toml  # Poetry configuration
└── README.md       # This file
```

