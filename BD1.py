import flask
from flask import Flask, render_template, request, flash,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Sondage3.sqlite3'
app.config['SECRET_KEY'] = "random String";

db = SQLAlchemy(app)

class Sondage(db.Model):
    __tablename__ = 'Sondage'
    id_sondage = db.Column(db.Integer, primary_key=True)
    libele = db.Column(db.String(20), nullable=False)
    id_user = db.Column(db.Integer, primary_key=True)
    
    

class Utilisateur(db.Model):
    __tablename__ = 'Utilisateur'
    id_user = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(20), nullable=False)
    mail = db.Column(db.String(20), nullable=False)
    mot_de_passe = db.Column(db.String(20), nullable=False)
     

               
class Question(db.Model):
    __tablename__ = 'Question'
    id_sondage = db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    intitule_question = db.Column(db.String(20), nullable=False)
    

class Choix(db.Model):
    __tablename__ = 'Choix'
    id_sondage = db.Column(db.Integer, primary_key=True)
    id_choix = db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, primary_key=True)
    intitule_choix = db.Column(db.String(20), nullable=False)
    nbre_reponses=db.Column(db.Integer, primary_key=True)

                
                
with app.app_context():
    db.create_all()
    app.run(debug=True, port=4000)
