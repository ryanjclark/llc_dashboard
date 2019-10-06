from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://swealcdt_sa:ridgewayequity@thesweatconnection.com:2083/swealcdt_production'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class Tsc(db.Model):
    __tablename__ = 'alert_funnel'
    id = db.Column('id', db.Integer, primary_key=True)
    email_alert = db.Column('email_alert', db.Unicode)

if __name__ == "__main__":
    manager.run()