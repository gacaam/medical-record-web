# Medical Records System

## Overview

This project is a medical records management system built with FastAPI. It allows for CRUD operations on medical records, including viewing, creating, updating, and deleting records. The system includes a basic frontend for interacting with the API and managing records.

## Features

- **View Medical Records:** Access all records in the database.
- **Create New Record:** Add a new medical record to the database.
- **Update Record:** Modify existing medical records.
- **Delete Record:** Remove medical records from the database.

## Project Structure

- **main.py:** Contains the FastAPI application and API endpoints.
- **static/**: Directory for static files like HTML, CSS, and JavaScript.
  - **index.html:** Home page.
  - **database.html:** Page to view all medical records.
  - **create_record.html:** Form to create new records.
  - **edit_record.html:** Form to update existing records.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gacaam/medical-record-web.git
   cd medical-record-web
   ```

2. **Create and activate virtual environment**:
    ```sh
    python -m venv env
    .\env\Scripts\activate # Windows
    source automatedtest/bin/activate  # macOS/Linux
    ```
3. **Install required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    uvicorn main:app --reload
    ```   
    The application will be accessible at http://127.0.0.1:8000.

