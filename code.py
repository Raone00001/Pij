# Importing all modules
from flask import Flask,jsonify, request

# For installing
# -- python -m venv venv
# -- pip install flask

# This is like a constructor off the class flask. It takes the name of the current module.
app = Flask(__name__)

# Array 
contacts = [
    {
        'id': 1,
        'Name': u'User1',
        'Contact': u'9997778888', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'User2',
        'Contact': u'9996668888', 
        'done': False
    }
]

# route() of Flask is like a decorator which will tell our web app which url is associated with it (the function too). 
@app.route("/")
def hello_world():
    return "Hello World!"

# We are specifying what we want to have on the root. 
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    
# If we run this, we will see all the tasks we gave at the top.
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

# To run the code on our web application, we can say app.run(). To say the next changes, we added "debug=True". 
if (__name__ == "__main__"):
    app.run(debug=True)