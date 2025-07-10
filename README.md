# Web Application Setup Guide

This guide will help you run the web application locally.

## Prerequisites

- Python 3.9.0 (or compatible version) installed
- `pip` (Python package manager)

## Getting Started

1. **Open your terminal or command prompt.**

2. **Navigate to the directory where the project files are located.**  
   For example:

   ```bash
   cd Downloads
   cd projectFinal
   ```

3. **Install project dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**

   Once the server is running, open your browser and visit:  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

   You should now have access to the web application locally.

## Notes

- Make sure all required files are in the same directory.
- If you encounter any issues, check your Python version or virtual environment setup.

