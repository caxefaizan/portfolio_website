from flask import Flask, render_template, request, redirect, send_from_directory
import csv, json
from datetime import date
from flask_mail import Mail, Message

app = Flask(__name__)

with open("./profiledata.json", "r") as fp:
    data = json.loads(fp.read())
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
    print(f'{data["basic"]["name"].lower().replace(" ","")}')
    return send_from_directory(
        directory="./static/assets/downloads",
        path=f'{data["basic"]["name"].lower().replace(" ","")}-resume.pdf',
        as_attachment=True,
    )


@app.route(
    "/"
)  # for loading templates, default folder it looks from and necesary is templates also for css,js,favicon those should be in static folder
def webpage():
    return render_template("index.html", data=data)


@app.route(
    "/2"
)  # for loading templates, default folder it looks from and necesary is templates also for css,js,favicon those should be in static folder
def webpage2():
    return render_template("indexs.html", data=data)


def write_to_csv(data):
    try:
        msg = Message(
            f"{name}", sender=user_id, recipients=["faizanzahid09@hotmail.com"]
        )
        msg.body = f"Hi Faizan,\n{name}: {email} has dropped in the following message for you.\n{message}"
        mail.send(msg)
    except:
        with open("./database.csv", newline="", mode="a") as database:
            email = data["email"]
            name = data["name"]
            message = data["message"]
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
            return redirect("/thankyou.html")
        except Exception as e:
            return str(e) + "did not save in database"
    else:
        print("Something wrong")
