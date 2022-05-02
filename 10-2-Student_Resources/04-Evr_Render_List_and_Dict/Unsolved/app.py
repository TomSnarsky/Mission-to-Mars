# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)

# @TODO: Create a list of dictionaries
dogs = []
dogs.append({"name": "Fido", "type": "Lab"})
dogs.append({"name": "Tucker", "type": "Golden"})
dogs.append({"name": "Asparagus", "type": "Cat"})

# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
@app.route("/")
def echo():
    return render_template("index.html", dogs=dogs)


if __name__ == "__main__":
    app.run(debug=True)
