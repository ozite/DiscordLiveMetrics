from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import DiscordLiveMetrics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id



@app.route('/', methods= ['Post', 'GET'])
def index():
    if request.method == 'POST':
        return DiscordLiveMetrics.plot()

    else:
        pass

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
