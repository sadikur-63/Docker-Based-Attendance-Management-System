# Docker-Based Attendance Management System

A simple web-based attendance management system built with Python, Flask, SQLite, HTML, CSS, JavaScript, and Docker.

This project was developed as a university learning project to demonstrate web application development, backend integration, database storage, and local containerization using Docker.

## Project Overview

The Docker-Based Attendance Management System allows users to record student attendance and view attendance records through a web dashboard.

The application runs locally on a computer using Docker.

## Features

- Web-based attendance dashboard
- Record student attendance
- Mark students as Present or Absent
- Store attendance records in an SQLite database
- View saved attendance records
- Display total, present, and absent counts
- Flask backend API
- Docker containerization
- Local database persistence using a Docker volume

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web server and API |
| SQLite | Attendance database |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Dashboard interaction |
| Docker | Application containerization |
| Docker Compose | Running the application |
| Gunicorn | Python application server |

## System Architecture

The application follows this basic architecture:

    User
      |
      v
    Web Dashboard
      |
      v
    Flask Backend API
      |
      v
    SQLite Database

Docker runs the backend application in a container. The dashboard communicates with the backend to save and retrieve attendance records.

## Project Structure

    docker-attendance/
    ├── app.py
    ├── Dockerfile
    ├── compose.yaml
    ├── requirements.txt
    ├── .gitignore
    ├── .dockerignore
    ├── README.md
    ├── data/
    │   └── .gitkeep
    └── static/
        └── index.html

## Requirements

Before running the project, install:

- Docker Desktop
- Git (optional, for cloning the repository)
- A modern web browser

## Installation and Setup

### 1. Clone the repository

Open a terminal and run:

    git clone https://github.com/sadikur-63/Docker-Based-Attendance-Management-System.git

### 2. Enter the project directory

    cd Docker-Based-Attendance-Management-System

### 3. Build and start the application

    docker compose up --build -d

Docker Compose will build the application image and start the container.

### 4. Open the dashboard

Open your web browser and visit:

    http://localhost:5000

You can now use the attendance dashboard.

## How to Use

1. Open the attendance dashboard.
2. Enter the Student ID.
3. Select the attendance date.
4. Enter the Course ID.
5. Select Present or Absent.
6. Click Save Attendance.
7. Check the attendance summary and records table.

## API Endpoints

### Get Attendance Records

    GET /attendance

Returns saved attendance records in JSON format.

### Save Attendance

    POST /attendance

Example JSON request:

    {
      "student_id": "STU001",
      "attendance_date": "2026-10-13",
      "course_id": "CLOUD101",
      "status": "present"
    }

Valid attendance statuses are `present` and `absent`.

## Database

The application uses SQLite to store attendance records.

The database contains fields for:

- Record ID
- Student ID
- Attendance date
- Course ID
- Attendance status
- Record creation time

The database file is stored in the local `data` directory when configured as described in `compose.yaml`.

## Docker Commands

Build and start the application:

    docker compose up --build -d

View running containers:

    docker compose ps

View application logs:

    docker compose logs -f

Stop the application:

    docker compose down

The database should remain available after stopping or recreating the container when the configured data volume is retained.

## Learning Objectives

This project demonstrates:

- Building a simple web application
- Creating a REST API with Flask
- Connecting a backend to a database
- Saving and retrieving attendance records
- Using Docker to package an application
- Running containers with Docker Compose
- Preparing an application for future cloud deployment

## Future Improvements

Possible future enhancements include:

- AI-assisted attendance analysis
- Email notifications for absent students
- User authentication
- Student and teacher accounts
- Cloud database integration
- AWS cloud deployment
- Improved reporting and analytics

These features are future improvements and should not be considered implemented in the current version unless they are added separately.

## Project Status

**Current status:** Local Docker prototype.

The current version supports attendance recording and retrieval through a web dashboard. The project can be extended with cloud services and additional features in future development.

## Author

**Sadikur**

Information Technology Student

Developed for educational and university project demonstration purposes.
