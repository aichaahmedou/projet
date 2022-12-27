import flask
from flask import Flask, render_template, request, flash,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Sondage.sqlite3'
app.config['SECRET_KEY'] = "random String";

db = SQLAlchemy(app)

class Sondage(db.Model):
    __tablename__ = 'Sondage'
    id_sondage = db.Column(db.Integer, primary_key=True)
    libele = db.Column(db.String(20), nullable=False)
    date_de_creation = db.Column(db.Date, nullable=False)
    date_de_dernier_modification = db.Column(db.Date, nullable=False)
    
    



class Utilisateur(db.Model):
    __tablename__ = 'Utilisateur'
    id_user = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.Date, nullable=False)
    mail = db.Column(db.String(20), nullable=False)
    mot_de_passe = db.Column(db.String(20), nullable=False)
    

        
        
class Vote(db.Model):
    __tablename__ = 'Vote'
    date_vote = db.Column(db.Date, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('Utilisateur.id_user'))
    id_sondage = db.Column(db.Integer, db.ForeignKey('Sondage.id_sondage'))
    mail = db.Column(db.String(20), nullable=False)
    

        
        
class Envoi(db.Model):
    __tablename__ = 'Envoi'
    date_envoi = db.Column(db.Date, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('Utilisateur.id_user'))
    id_sondage = db.Column(db.Integer, db.ForeignKey('Sondage.id_sondage'))
   
    

        
class Proposition(db.Model):
    __tablename__ = 'Proposition'
    id_proposition = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.String(20), nullable=False)
    id_QCM = db.Column(db.Integer, db.ForeignKey('QCM.id_QCM'))

    

               
class Question(db.Model):
    __tablename__ = 'Question'
    id_question = db.Column(db.Integer, primary_key=True)
    intitule_question = db.Column(db.String(20), nullable=False)
    


class Reponse_text (db.Model):
    __tablename__ = 'Reponse_text'
    id_reponse_text=db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer, db.ForeignKey('QCM.id_QCM'))
    reponse = db.Column(db.String(20), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('Utilisateur.id_user'))



class QCM(db.Model):
    __tablename__ = 'QCM'
    id_QCM= db.Column(db.Integer, primary_key=True)
    intitule_QCM = db.Column(db.String(20), nullable=False)


          
class Reponse(db.Model):
    __tablename__ = 'Reponse'
    id_reponse=db.Column(db.Integer, primary_key=True)
    id_QCM = db.Column(db.Integer, db.ForeignKey('QCM.id_QCM'))
    id_proposition = db.Column(db.Integer, db.ForeignKey('Proposition.id_proposition'))
    id_user = db.Column(db.Integer, db.ForeignKey('Utilisateur.id_user'))

                
                
with app.app_context():
    db.create_all()
    app.run(debug=True, port=4000)
