from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS= [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': ' Mumbai, India',
        'salary': ' Rs. 10,00,000'
    },
        {
        'id': 2,
        'title': 'Data Scientist',
        'location': ' Delhi, India',
        'salary': ' Rs. 15,00,000'
    },
        {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': ' Remote',
        'salary': ' Rs. 120,000'
        
    },
        {
        'id': 4,
        'title': 'Backend Engineer',
        'location': ' California, USA',
        'salary': ' $120,000'
    },
    
]

@app.route('/')
def hello_world():
    return render_template("index.html", jobs = JOBS )

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)