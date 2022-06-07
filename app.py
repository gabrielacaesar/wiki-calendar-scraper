import os
from flask import Flask, request
from scraper_calendar import get_events

# coisas do site
app = Flask(__name__)

@app.route("/")
def hello_world():
	arquivo = open("templates/home.html")
	return arquivo.read()


months = ["june", "july", "august"]

for month in months:
f"""@app.route('/en-{month}')"""
f"""def display_en-{month}():"""
	f"""events = get_events({month}, 'en')"""
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
	events = get_events("juni", "de")
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
