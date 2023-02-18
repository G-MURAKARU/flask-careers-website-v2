from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def home_page():
	# in order to render dynamic content into a html page, provide arguments to the render_template function
	return render_template('home.html', jobs=load_jobs_from_db(), title='Home')


@app.route("/api/jobs")
def list_jobs():
	return jsonify(load_jobs_from_db())


@app.route("/job/<id>")
def show_job(id):
	job = load_job_from_db(id)
	return render_template('job_page.html', job=job, title=job['title'])


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
