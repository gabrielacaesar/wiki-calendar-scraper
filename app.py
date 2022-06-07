import os
from flask import Flask, request
from scraper_calendar import get_events

# coisas do site
app = Flask(__name__)

@app.route("/")
def hello_world():
	arquivo = open("templates/home.html")
	return arquivo.read()

@app.route("/calendar")
def display_events():
	events = get_events("maio", "pt")
	return f"""
	<p>{events}</p>
	"""
