from flask import Flask, render_template, request, jsonify
from config import WEATHER_KEY, GEO_KEY
import requests
import config

app = Flask(__name__)

# Function to get weather data from OpenWeather
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if data.get('cod') != 200:
        return None  # City not found or error in API request

    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'pressure': data['main']['pressure'],
        'weather': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }
    return weather

@app.route('/get-api-key', methods=['GET'])
def get_geo_api_key():
    return jsonify({
        'api_key': GEO_KEY
    })



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-weather', methods=['GET'])
def get_weather_data():
    city = request.args.get('city')
    weather = get_weather(city)
    
    if weather:
        return jsonify(weather)
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
