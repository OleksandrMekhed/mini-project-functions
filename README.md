# Service Status Monitor

A lightweight, modular command-line tool written in Python designed to monitor, list, and report the operational statuses of various local or containerized services (such as Nginx, PostgreSQL, Redis, Docker, etc.).

## Features

* **Interactive CLI Menu:** A clean text-based loop allowing users to easily navigate options.
* **Service Lookup:** View all registered services or query a specific service by name.
* **Status Reporting:** Generate a comprehensive health report verifying service statuses (`OK` / `WRONG`).
* **Modular Architecture:** Clean separation of concerns across multiple focused modules.

---

## Project Structure

```text
service_status_monitor/
│
├── main.py          # Application entry point (runs the menu loop)
├── menu.py          # Interactive UI and user choice handling
├── report.py        # Generates and prints service health reports
├── check_service.py # Validates and formats individual service statuses
└── services.py      # Mock dataset and service lookup logic
```

## Requirements

* **Python 3.8+** (uses the standard library only, no external dependencies required).

## Installation & Running

1. **Clone the repository** (or download the files into a single directory):

   ```bash
   git clone https://github.com/OleksandrMekhed/mini-project-functions.git
   cd mini-project-functions
   ```

2. **Run the application:**

   ```bash
   python main.py
   ```

## Usage

Once you run `python main.py`, you will see the interactive menu:

```text
------------------------------
--- Welcome to the menu ---
1. Show all services
2. Show one service
3. Show report
4. Exit
------------------------------
Enter your choice:
```

Simply type the number corresponding to your desired action.

## Tech Stack

* **Language:** Python 3
* **Design Pattern:** Modular programming, Separation of Concerns