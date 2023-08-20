from flask import Flask, render_template

app = Flask(__name__)

Jobs = [{
  'id': 1,
  'title': 'Data Scientist',
  'Location': 'Bengalore',
  'Salary': '1,00,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'Location': 'Chennai',
  'Salary': '50,000'
}, {
  'id': 3,
  'title': 'Full-Stack Developer',
  'Location': 'Delhi',
  'Salary': '70,000'
}, {
  'id': 4,
  'title': 'Frontend Developer',
  'Location': 'Pune',
  'Salary': '35000'
}]


@app.route("/")
def home():
  return render_template("home.html", jobs=Jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
