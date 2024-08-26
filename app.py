from flask import Flask, render_template, jsonify

app = Flask(__name__)
# add dynamic data structure
JOBS =[
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Briston UK",
        "salary": "£38,000"
    },
    {
        "id": 2,
        "title": "IT technician",
        "location": "London UK",
        "salary": "£35,000"
    },
    {
        "id": 3,
        "title": "Customer service",
        "location": "Hybrid remote",
        "salary": "25,000"
    },
    {
        "id": 4,
        "title": "Front end developer",
        "location": "Remote",
        "salary": "£30,000"
    },
    {
        "id" : 5,
        "title": "Back end developer",
        "location": "Remote",
        "salary": "£35,000"
    }
]
@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)
# added an api route
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
  app.run (host = "0.0.0.0", debug = True)