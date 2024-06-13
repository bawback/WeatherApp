# Weather App

## About The Project
This is a simple Flask application that retrieves weather information based on city names. It uses the OpenWeatherMap API to fetch weather data.

## Getting Started
Here is how to get started:

### Prerequisites
- Python 3.8+
- Flask
- Requests library

### Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Configuration

### Setting Up Environment Variables

To run this project, you will need to add the following environment variable to your .env file:

`OPENWEATHER_API_KEY`

You can obtain an API key by registering at [OpenWeatherMap](https://openweathermap.org/). After registration, navigate to your API keys and copy your key.

#### Creating the .env file

1. Create a file named `.env` in the root directory of the project.
2. Open the `.env` file in a text editor.
3. Add the following line to the file:

   ```bash
OPENWEATHER_API_KEY=your_api_key_here
   ```
Replace `your_api_key_here` with the API key you obtained from OpenWeatherMap.

This will allow the application to access the OpenWeatherMap API using your key while keeping the key secure and out of source control.

## Usage
Here is how to use:

Run the application:
   ```bash
   python app.py
   ```

Open your web browser and go to http://127.0.0.1:5000/ to see the app in action.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Boback Khoshnevis - bkhoshnevis@gmail.com
