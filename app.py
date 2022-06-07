import os
from flask import Flask, request
from scraper_calendar import get_events

# coisas do site
app = Flask(__name__)

@app.route("/")
def hello_world():
	
	return arquivo.read()

@app.route("/en")
def display_en():
	events = get_events("maio", "en")
	return f"""
	<p>{events}</p>
	"""

@app.route("/calendar")
def display_events():
	events = get_events("maio", "pt")
	return f"""
	<tr>
	<td>{events[0]}</td>
	</tr>
	"""
