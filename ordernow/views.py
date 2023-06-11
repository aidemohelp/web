from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.htlm",name= "mothushi")

@views.route("/profile/")
def profile(username):
    args = request.args
    name = args.get('name')
    return render_template("index.htlm", name=name)

@views.route("/json")
def get_json():
    return jsonify({'name': 'mothushi finna get what you gazing for madafaker'})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))