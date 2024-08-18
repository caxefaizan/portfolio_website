from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
    redirect,
    url_for,
)
import csv, json
from datetime import date
from flask_mail import Mail, Message
from docwriter import generate_resume_doc

app = Flask(__name__)

with open("./profiledata.json", "r") as fp:
    profile_data = json.loads(fp.read())
with open("./config.txt", "r") as fp:
    conf = fp.read()

user_id = "caxedummy@gmail.com"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = user_id
app.config["MAIL_PASSWORD"] = conf
app.config["MAIL_USE_SSL"] = True

mail = Mail(app)


# route to serve the first .exe file
@app.route("/download/resume")
def download_file():
    generate_resume_doc(profile_data)
    return send_from_directory(
        directory="./static/assets/downloads",
        path=f'{profile_data["basic"]["name"].lower().replace(" ","")}-resume.docx',
        as_attachment=True,
    )


@app.route("/")
def webpage():
    return render_template("index.html", data=profile_data)


def write_to_csv(data):
    email = data["email"]
    name = data["name"]
    message = data["message"]
    try:
        msg = Message(
            f"{name}", sender=user_id, recipients=[profile_data["basic"]["email"]]
        )
        msg.body = f"Hi {profile_data['basic']['name']},\n{name}: {email} has dropped in the following message for you.\n{message}"
        mail.send(msg)
    except:
        with open("./database.csv", newline="", mode="a") as database:
            csv_writer = csv.writer(
                database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            csv_writer.writerow([email, name, message, date.today()])


@app.route("/submit_form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
        except Exception as e:
            return str(e) + "did not save in database"
    else:
        print("Something wrong")
    return redirect(url_for("webpage"))


if __name__ == "__main__":
    app.run(debug=True)
