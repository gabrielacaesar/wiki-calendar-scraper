import os
from flask import Flask, request, jsonify, after_this_request
from scraper_calendar import get_events
import flask, json

# coisas do site
app = Flask(__name__)

@app.route("/")
def hello_world():
	arquivo = open("templates/home.html")
	return arquivo.read()

@app.route("/eventos", methods=['GET'])
def get_content():
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        
    month = str(request.args['month'])
    lang = str(request.args['lang'])

    try:
        output = get_events(month, lang)

    except ValueError as e:
        return {"error":1}

    return jsonify(output)

@app.route("/en-june")
def display_en():
	events = get_events("June", "en")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

@app.route("/pt-junho")
def display_pt():
	events = get_events("junho", "pt")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

@app.route("/de-juni")
def display_de():
	events = get_events("Juni", "de")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

@app.route("/es-junio")
def display_es():
	events = get_events("junio", "es")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""

@app.route("/calendar")
def display_events():
	events = get_events("maio", "pt")
	html_events = events.to_html()
	return f""""
	{html_events}
	"""
