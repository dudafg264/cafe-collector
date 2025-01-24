# Cafe Collector

A Flask-based web application to collect and display information about cafes, including their name, location, opening and closing times, and ratings for coffee, WiFi, and power availability.

---

## Overview

Cafe Collector allows users to:
- Add information about cafes via a form.
- Store the data in a CSV file.
- Display the list of cafes dynamically on a webpage.

---

## Features

- **Form Submission**: Users can input details about a cafe through a web form.
- **Data Storage**: Cafe information is saved to a CSV file (`cafe-data.csv`).
- **Dynamic Display**: A webpage displays the list of cafes from the CSV file.
- **Ratings**: Options to rate coffee, WiFi, and power availability.

---

## Technologies Used

- **Python** (Flask): Backend framework to manage routes and handle form submissions.
- **Flask-Bootstrap**: To style the application.
- **Flask-WTF**: For form handling and validation.
- **HTML/CSS**: Frontend for rendering the webpages.
- **CSV**: Used as the data storage format.

---

## Usage

### Adding a Cafe
1. Go to `/add` by clicking the "Add Cafe" link or entering the URL.
2. Fill out the form with the cafe's details:
   - Name
   - Location (Google Maps URL)
   - Opening and closing times
   - Coffee, WiFi, and power ratings
3. Click **Submit** to save the details.

### Viewing the Cafe List
1. Go to `/cafes` to see the list of all added cafes.
2. Each row in the table represents a cafe, showing its details and ratings.

---

## File Structure

```
cafe-collector/
│
├── templates/
│   ├── base.html          # Base layout for the application
│   ├── index.html         # Homepage template extending base.html
│   ├── add.html           # Form template to add a cafe
│   └── cafes.html         # Displays the list of cafes
│
├── static/                # Static assets
│
├── cafe-data.csv          # Stores cafe information
│
├── main.py                # Main application file
│
└── README.md              # Documentation file
```

