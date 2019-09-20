from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)



@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    query = request.args.get('q')
    # TODO: Make 'params' dict with query term and API key
    params = {
    "q": query,                     #tells tenor the keyword you want to search
    "key": "U78L9P5SJIJZ",          #lets you access tenor with the api key
    "limit":10                      #tells pc how many gifs u want
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    response = requests.get('https://api.tenor.com/v1/search', params=params) #adds params items to the end of the url      #response is an object misc response info
    # TODO: Get the first 10 results from the search results
    response_json = response.json()       #converts response info into giant json dictionary
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("index.html", results = response_json["results"])               #links the index.html file to this function and passes the json dic into index html


if __name__ == '__main__':
    app.run(debug=True)


#api key: U78L9P5SJIJZ 