from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
    Response,
)
import csv, json, os
from datetime import date
from flask_mail import Mail, Message
from docwriter import generate_resume_doc
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(_dir, "profiledata.json"), "r") as fp:
    profile_data = json.loads(fp.read())

user_id = os.environ["MAIL_USERNAME"]
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = user_id
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
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


@app.route("/robots.txt")
def robots():
    site_url = profile_data["basic"]["site_url"]
    body = f"User-agent: *\nAllow: /\nSitemap: {site_url}/sitemap.xml\n"
    return Response(body, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    site_url = profile_data["basic"]["site_url"]
    body = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{site_url}/</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>"""
    return Response(body, mimetype="application/xml")


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
    try:
        data = request.form.to_dict()
        write_to_csv(data)
        return "", 200
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(debug=True)
