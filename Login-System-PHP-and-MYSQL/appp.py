from flask import Flask
import subprocess
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    output = subprocess.check_output(['php','index.php'])
    return output
app.run(debug=True)