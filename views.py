from flask import Blueprint, render_template, request, flash, redirect
import csv
import pandas as pd
views = Blueprint('views', __name__)

patients = []
l = []
users = []
new_users = []
emails = []
name = []


@views.route('/', methods=["GET", "POST"])
def login():
    email = request.form.get("email")
    emails.append(email)
    return render_template("login.html")

@views.route('/reg_patients')
def reg_patients():
    email = request.form.get("email")
    emails.append(email)
    name.append(emails[1].split('@'))
    return render_template('/reg_patients.html', email = name[0][0])

@views.route('/reg_patients', methods=["GET", "POST"])
def registered():
    firstName = request.form.get("firstName")
    lastName = request.form.get("lastName")
    gender = request.form.get("gender")
    description = request.form.get("description")
    name = (f"{firstName} {lastName}")
    patients.append(f"Name: {name} \nGender:{gender} \nDescription:{description}")
    file = open("patient_details.csv" ,"a")
    writer = csv.writer(file)
    writer.writerow((name, gender, description))
    file.close()
    return redirect('/reg_patients')

@views.route('/new_patients')
def new_patients():
    for patient in patients:
        if patient not in l:
            l.append(patient)
    return render_template("new_patients.html", patients = l)

# @views.route('/', methods=["GET", "POST"])
# def login():
#     email = request.form.get("email")
#     password = request.form.get("password")
#     users.append(f"{email} {password}")
#     for user in users:
#         if user not in new_users:
#             new_users.append(user)
#     print(new_users)
#     return render_template("base.html")


# @views.route('/home', methods=["POST"])
# def register():
#     firstName = request.form.get("firstName")
#     lastName = request.form.get("lastName")
#     gender = request.form.get("gender")
#     if not firstName or not lastName or not gender:
#         return "Failure"
#     file = open("patient_details.csv" ,"a")
#     writer = csv.writer(file)
#     writer.writerow((request.form.get("firstName"),request.form.get("lastName"), request.form.get("gender")))
#     file.close()
#     patients.append(f"{firstName} {lastName} gender:{gender}")
#     return render_template("home.html")