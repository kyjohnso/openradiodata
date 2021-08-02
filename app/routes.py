from flask import render_template, url_for, request, jsonify
from app import app, db
from app.models import Raw, Fix, Test

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title="Open Radio Data")

@app.route('/raw/', methods=['GET', 'POST'])
def raw():
    return "no raw data"    


@app.route('/api/test', methods=['GET', 'POST'])
def api_test():
    if request.method == 'POST':
        test_json = request.get_json(force=True)
        test = Test(**test_json)
        print(test)
        db.session.add(test)
        db.session.commit()
        return "success"
    else:
        tests = Test.query.all()
        if type(tests) == list:
            tests = [t.to_dict() for t in tests]
        return jsonify(tests)

