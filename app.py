from flask import Flask, render_template, jsonify

app = Flask(__name__)

# database simulation
JOBS = [
 {
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Nairobi, Kenya',
  'salary': 'ksh 60,000'
 },
 {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Mombasa, Kenya',
  'salary': 'ksh 120,000'
 },
 {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'Remote',
  'salary': 'ksh 100,000'
 },
 {
  'id': 4,
  'title': 'Frontend Engineer',
  'location': 'Isiolo, Kenya'
 },
]


@app.route("/")
def hello_world():
	# in order to render dynamic content into a html page, provide arguments to the render_template function
	return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
	return jsonify(JOBS)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
