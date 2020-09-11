#import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

app = Flask(__name__)

#app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_data"
#mongo = pymongo(app)

# setup mongo connection
# connect to mongo db and collection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_data
#mongo = pymongo(app, uri="mongodb://localhost:27017/mars_data")


@app.route("/")
def index():
    mars_data = pymongo.db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
    scrape_data = scrape_mars.scrape()
    pymongo.db.mars_data.update({}, mars_data, upsert=True)
    return redirect ("/")


if __name__ == "__main__":
    app.run(debug=True)
