# Weather-Data-Fetcher


# Weather Data Fetcher

Weather Data Fetcher is a Python-based project designed to collect and store weather information from the OpenWeatherMap API and save it in a MySQL database. This project is particularly useful for developers and data analysts who need to gather weather data for multiple cities and store it in a structured database format for further analysis or application use. The project ensures that data is consistently fetched and stored, with robust error handling and logging mechanisms to track the process.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Scheduled Data Fetching](#scheduled-data-fetching)
- [Retrieve Data](#retrieve-data)
- [License](#license)

## Features

- Fetches weather data from the OpenWeatherMap API.
- Stores weather data in a MySQL database.
- Modular code for easy configuration management.
- Error handling and logging.

## Prerequisites

- Python 3.7 or higher
- MySQL Server
- Required Python packages (`requests`, `mysql-connector-python`)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/weather-data-fetcher.git
    cd weather-data-fetcher
    ```

2. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**

    Create a `config.py` file in the project directory and add your OpenWeatherMap API key and MySQL database credentials:

    ```python
    # config.py

    # API configuration
    API_URL = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = "your_openweather_api_key"  # Replace with your OpenWeatherMap API key

    # Database configuration
    DB_HOST = "localhost"
    DB_USER = "your_db_username"
    DB_PASSWORD = "your_db_password"
    DB_NAME = "your_db_name"
    ```

4. **Initialize the database:**

    Ensure your MySQL server is running and you have created the database specified in the `config.py` file. Run the following command to create the required table:

    ```sh
    python main.py
    ```

## Usage

1. **Fetch and store weather data:**

    Run the `main.py` script to fetch weather data and store it in the database:

    ```sh
    python main.py
    ```

## Configuration

- **`config.py`**: Stores configuration details like API keys and database connection parameters.
- **`database.py`**: Contains functions to connect to the database, create the table, and insert data.
- **`main.py`**: Contains the main script to fetch weather data from the API and store it in the database.

### Example `config.py`

```python
# config.py

# API configuration
API_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "your_openweather_api_key"  # Replace with your OpenWeatherMap API key

# Database configuration
DB_HOST = "localhost"
DB_USER = "your_db_username"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"
