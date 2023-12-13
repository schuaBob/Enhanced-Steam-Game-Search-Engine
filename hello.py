from flask import Flask
from indexing.IndexReader import MyIndexReader
import argparse

app = Flask(__name__)
indexReader = MyIndexReader()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/search/<query>")
def search(query):
    search_results = indexReader.search(query)
    return f"<p>Result: {search_results}</p>"