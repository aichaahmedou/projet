from flask import Flask,render_template,request
from flask_mail import Mail
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
app=Flask(__name__)
app.config['DEBUG']=True
#app.config['TESTING']=False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
#app.config['MAIL-DEBUG']=True
app.config['MAIL_USERNAME']='21060@supnum.mr'
app.config['MAIL_PASSWORD']='ysbwbwmxxewtgfsv' 
#app.config['MAIL_DEFAULT_SENDER']='21060@supnum.mr'
#app.config['MAIL_MAX_EMAILS']=None
#app.config['MAIL_SUPRESS_SEND']=False
#app.config['MAIL_ASCII_ATTACHMENTS']=False
mail=Mail(app)
@app.route('/')
def index():
    msg=Message('object',sender='21060@supnum.mr',recipients=['21030@supnum.mr'])
    msg.body="email sla7 l7mdllh"
    mail.send(msg)
    return 'sent'

app.run(debug=True)
