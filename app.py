from flask import Flask, request
import json
import dbhelpers

app = Flask(__name__)

@app.get("/api/philosopher")
def return_philo():
    results = dbhelpers.run_procedures("CALL return_philosopher()", [])
    if(type(results) == list):
        philosopher_json = json.dump(results, default=str)
        return philosopher_json
    else:
        return "sorry, something went wrong"
app.run(debug=True)