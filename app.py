# Importing Flask libraries:
from flask import Flask, redirect, url_for, request, render_template, request, template_rendered

import requests

from dotenv import dotenv_values


#pulling saved API key from environment:
config = dotenv_values(".env")
API_key = (config["weather_api"])

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("index.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        city_name = request.form['city']
        # pulling API data from openweathermap API:
        if city_name:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
# if status_code is 200, weather data is generated as a json response, converted from kelvin to celcius temperature
            # with round() method, rendered via a template and displayed via result.html:
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                temperature_celsius = round(weather_data['main']['temp'] - 273.15, 2)
                return render_template('result.html', weather=weather_data, temperature=temperature_celsius)
            else:
                return "Location not found. Please try again."

        return "Please enter a city name."

    return render_template('search.html')



@app.route("/map")
def map():
    return(render_template('map.html'))

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/location")
def location():
    return render_template('location.html')


@app.route("/login", methods=["POST", "GET"])
def login():
     if request.method == "POST":
         user = request.form["nm"]
         return redirect(url_for("user", usr=user))
     else:
         return render_template('login.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)











