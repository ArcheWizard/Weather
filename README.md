# Weather Application

A modern, responsive weather application built with Flask and JavaScript that provides real-time weather information using the OpenWeather API and location autocomplete using the OpenCage Geocoding API.

## Features

- Real-time weather data retrieval
- Location autocomplete with keyboard navigation
- Detailed weather information display including:
  - Current temperature
  - "Feels like" temperature
  - Humidity levels
  - Wind speed
  - Atmospheric pressure
- Responsive design with Tailwind CSS
- Loading states and error handling
- Weather condition icons
- Smooth animations and transitions

## Technical Stack

### Backend

- Flask 3.1.0
- Python 3.x
- RESTful API architecture

### Frontend

- HTML5
- JavaScript (Vanilla)
- Tailwind CSS
- Google Fonts (Roboto)

### APIs

- OpenWeather API for weather data
- OpenCage Geocoding API for location autocomplete

## Prerequisites

Before running the application, ensure you have:

- Python 3.x installed
- OpenWeather API key
- OpenCage Geocoding API key

## Installation

1. Clone the repository:

    ```bash
    git clone [repository-url]
    cd weather-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `config.py` file in the root directory with your API keys:

```python
WEATHER_KEY = "your_openweather_api_key"
GEO_KEY = "your_opencage_api_key"
```

## Running the Application

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to:

``
http://localhost:5000
``

## Project Structure

``
weather-app/
├── app.py              # Flask application and backend logic
├── requirements.txt    # Python dependencies
├── config.py          # API keys and configuration
└── templates/
    └── index.html     # Frontend interface
``

## API Endpoints

### GET `/get-weather`

Retrieves weather data for a specified city.

Parameters:

- `city` (string): Name of the city

Response:

```json
{
    "city": "City Name",
    "temperature": 20.5,
    "feels_like": 19.8,
    "humidity": 65,
    "wind_speed": 5.2,
    "pressure": 1013,
    "weather": "clear sky",
    "icon": "01d"
}
```

### GET `/get-api-key`

Retrieves the OpenCage API key for frontend geocoding.

Response:

```json
{
    "api_key": "your_opencage_api_key"
}
```

## Error Handling

The application includes comprehensive error handling for:

- Invalid city names
- API failures
- Network issues
- Empty search queries

## Security Considerations

- API keys are stored server-side in `config.py`
- OpenCage API key is only exposed to frontend for autocomplete functionality
- Input sanitization for city names
- Error messages don't expose sensitive information

## Browser Compatibility

The application is tested and works on:

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
