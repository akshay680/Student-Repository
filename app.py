# Import libraries
from flask import Flask, render_template
# Create app object
app = Flask(__name__)
# Define a decorator with '/'
@app.route("/")
def data():
    # Define data that has to be displayed on the html page
    data = [{"Student":"Bezos,J","CWID":10115,"Course":"SSW 810","Grade":"A","Instructor":"Rowland,J"},
                    {"Student":"Bezos,J","CWID":10115,"Course":"CS 546","Grade":"F","Instructor":"Hawking,S"},
                    {"Student":"Gates,B","CWID":11714,"Course":"CS 546","Grade":"A","Instructor":"Cohen,R"},
                    {"Student":"Gates,B","CWID":11714,"Course":"SSW 810","Grade":"B-","Instructor":"Rowland,J"},
                    {"Student":"Gates,B","CWID":11714,"Course":"CS 570","Grade":"A-","Instructor":"Hawking,S"},
                    {"Student":"Jobs,S","CWID":10103,"Course":"SSW 810","Grade":"A-","Instructor":"Rowland,J"},
                    {"Student":"Jobs,S","CWID":10103,"Course":"CS 501","Grade":"B","Instructor":"Hawking,S"},
                    {"Student":"Mush,E","CWID":10183,"Course":"SSW 555","Grade":"A","Instructor":"Rowland,J"},
                    {"Student":"Mush,E","CWID":10183,"Course":"SSW 810","Grade":"A","Instructor":"Rowland,J"},
                    ]
    # Call base.html and pass data as parameter to iterate and display on page
    return render_template("base.html", data=data)

# Check if it is main program
if __name__ == "__main__":
    # Run flask application on local host with debug mode enabled
    app.run(debug=True)    