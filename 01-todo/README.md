# Todo Django Project

A simple Todo application built with Django.

## Description

This project is a task management application that allows users to create, view, update, and delete todo items. It features a Django backend with an admin panel for management.

## Prerequisites

- Python 3.8+
- Django 5.2+

## Installation

1.  Clone the repository.
2.  Navigate to the project directory:
    ```bash
    cd 01-todo
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

This project includes a `Makefile` to simplify common commands.

### Running the Application

To start the development server:

```bash
make run
```

Or directly:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

### Database Migrations

To apply database migrations:

```bash
make migrate
```

Or directly:

```bash
python manage.py migrate
```

To create new migrations after modifying models:

```bash
make migrations
```

Or directly:

```bash
python manage.py makemigrations
```

### Admin User

To create a superuser for the admin panel:

```bash
make superuser
```

Or directly:

```bash
python manage.py createsuperuser
```

### Setup

To run migrations and create a superuser in one step:

```bash
make setup
```

## Features

-   **Todo Items**: Create, read, update, and delete tasks.
-   **Admin Panel**: Manage tasks via the Django admin interface (`/admin`).
-   **Task Status**: Mark tasks as completed or pending.
-   **Due Dates**: Set due dates for tasks.
