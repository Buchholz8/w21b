#for all of my requestes for some reason i am getting error 500 for my sever, im fairly certain everything is spelled correctly and is written atleast mostly correct
#i cant seem to find the error in this


#these are the imports
from flask import Flask, request, make_response
import json, jsonify
import dbhelpers

app = Flask(__name__)
#the first get request will send a request that will run the sql procedure called return_philosopher
@app.get("/api/philosopher")
def return_philo():
    results = dbhelpers.run_procedures("CALL return_philosopher()")
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 400)
#the first post request runs by calling the sql procedure called new_philosopher needing 5 jsons this also has the make_response
app.post("/api/philosopher")
def create_philosopher():
    error = dbhelpers.check_endpoint_info(request.json, ["name", "bio", "date_of_birth", "date_of_death", "image_url"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedures("call new_philosopher(?,?,?,?,?)", [request.json.get('name'), request.json.get('bio'), request.json.get('date_of_birth'), request.json.get('date_of_death'), request.json.get('image_url')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something has gone wrong"))
#the second get request calls the sql procedure called return_all this will return all of the qoutes   
@app.get("/api/qoute")
def return_qoutes():
    results = dbhelpers.run_procedures("CALL return_all()")
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 400)
#the seconf post calls the sql procedure new_philosopher this will create a new philosopher it needs 2 jsons and it has the make_response
app.post("/api/qoute")
def create_qoutes():
    error = dbhelpers.check_endpoint_info(request.json, ["philosopher_id", "content"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedures("call new_philosopher(?,?)", [request.json.get('philosopher_id'), request.json.get('content')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something has gone wrong"))
#i set up the debugger
app.run(debug=True)