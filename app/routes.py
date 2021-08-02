from flask import render_template, url_for, request, jsonify
from app import app, db
from app.models import Raw, Fix, Test

FORCE_JSON = True


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html", title="Open Radio Data")


@app.route("/raw/", methods=["GET", "POST"])
def raw():
    if request.method == "POST":
        raw_json = request.get_json(force=FORCE_JSON)
        if type(raw_json) == list:
            for raw in raw_json:
                raw_obj = Raw(**raw)
                db.session.add(raw_obj)
        else:
            raw_obj = Raw(**raw_json)
        db.session.commit()
        return jsonify({"success": True}), 200, {"ContentType": "application/json"}
    elif request.method == "GET":
        return "get raw not implemented yet"


@app.route("/fix/", methods=["GET", "POST"])
def fix():
    if request.method == "POST":
        fix_json = request.get_json(force=FORCE_JSON)
        if type(fix_json) == list:
            for fix in fix_json:
                fix_obj = Fix(**fix)
                db.session.add(fix_obj)
        else:
            fix_obj = Fix(**fix_json)
        db.session.commit()
        return jsonify({"success": True}), 200, {"ContentType": "application/json"}
    elif request.method == "GET":
        return "get fix not implemented yet"


@app.route("/api/test", methods=["GET", "POST"])
def api_test():
    if request.method == "POST":
        test_json = request.get_json(force=FORCE_JSON)
        print(type(test_json))
        if type(test_json) == list:
            for test in test_json:
                test_obj = Test(**test)
                db.session.add(test_obj)
        else:
            test_obj = Test(**test_json)
        db.session.commit()
        return jsonify({"success": True}), 200, {"ContentType": "application/json"}
    else:
        tests = Test.query.all()
        if type(tests) == list:
            tests = [t.to_dict() for t in tests]
        return jsonify(tests)
