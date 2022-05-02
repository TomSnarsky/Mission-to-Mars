from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    weather = mongo.db.weather_app.find_one()
    return render_template("index.html", weather=weather)

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    weather = mongo.db.weather_app
    weather_data = scrape_costa.scrape()

    # Update the Mongo database using update and upsert=True
    weather.update_one({}, {"$set": weather_data}, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
