from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "New Delhi, India",
    "salary": "Rs. 15,00,000"
}, {
    "id": 3,
    "title": "Backend Engineer",
    "location": "San Francisco, USA"
}, {
    "id": 4,
    "title": "Prompt Engineer",
    "location": "Remote (US)",
    "salary": "$ 500,000"
}]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)

# Following function returns a JSON object for the api url
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
