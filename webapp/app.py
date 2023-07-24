from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL
import settings



app = Flask(__name__)
db_url = URL.create(**settings.DATABASE)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db = SQLAlchemy(app)


class Estates(db.Model):
    id = db.Column( db.Integer, primary_key = True)
    title = db.Column(db.String())
    imgURL = db.Column(db.String())  

    def __init__(self, title, imgURL):
        self.title = title
        self.imgURL =  imgURL


@app.route('/')
def estate_index():
    estates = Estates.query.all()
    print(f"Showing {len(estates)}")

    return render_template("page.html", estate_list = estates)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 8080)


