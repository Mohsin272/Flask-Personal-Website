from flask import Flask, request, render_template
from appconfig import config
import DBcm

app = Flask(__name__)


@app.get("/")  # HTTP request : GET /
def index():
    return render_template("index.html", title="Welcome", heading="Welcome to my page")


@app.get("/personal")
def personal():
    return render_template(
        "personal.html", title="Personal", heading="Little Bit about Me"
    )


@app.get("/cv")
def cv():
    return render_template("cv.html", title="My CV", heading="My CV")


@app.get("/comptech")
def comptech():
    return render_template(
        "comptech.html",
        title="Computing Technologies",
        heading="Computing Technologies",
    )


@app.get("/comptech/python")
def comptechPython():
    return render_template(
        "python.html", title="Computing Technologies - Python", heading="Python"
    )


@app.get("/comptech/vsc")
def comptechVSC():
    return render_template(
        "vsc.html", title="Computing Technologies - VSC", heading="Visual Studio Code"
    )


@app.get("/comptech/java")
def comptechJava():
    return render_template(
        "java.html", title="Computing Technologies - Java", heading="Java"
    )


@app.get("/interests")
def interests():
    return render_template(
        "interests.html", title="My Interests", heading="My Interests"
    )


@app.get("/interests/cricket")
def interestsCricket():
    return render_template("cricket.html", title="Cricket", heading="Cricket")


@app.get("/interests/f1")
def interestsF1():
    return render_template("f1.html", title="Formula 1", heading="Formula 1")


@app.get("/form")
def form():
    return render_template("form.html", title="Contact Me")


@app.get("/display")
def view():
    with DBcm.UseDatabase(config) as db:
        SQL = """
    select email, message, date_format(time,"%m-%b-%Y %r") 
    from comments order by time desc;
        """
        db.execute(SQL)
        results = db.fetchall()
    return render_template(
        "view_comments.html", title="View Previous Comments", data=results
    )


@app.route("/processform", methods=["POST"])
def process():
    the_email = request.form["email"]
    the_message = request.form["message"]

    with DBcm.UseDatabase(config) as db:
        SQL = """
            insert into comments
            (email, message)
            values
            (%s, %s)
        """
        db.execute(SQL, (the_email, the_message))
    return render_template("thankyou.html", title="Thanks For Your Information")


if __name__ == "__main__":  # pragma no cover
    app.run(debug=True)
