from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        return redirect(url_for('weather', city=city))
    return render_template('index.html')

@app.route('/weather/<city>')
def weather(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
    weather_data = {}
    if response.status_code == 200:
        weather_data = response.json()
    else:
        weather_data = {'error': 'Cannot retrieve weather for this city'}
    return render_template('index.html', weather_data=weather_data, city=city)

if __name__ == '__main__':
    app.run(debug=True)
