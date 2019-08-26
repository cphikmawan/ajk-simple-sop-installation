from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for
import subprocess

app = Flask(__name__)
home = '/home/cloudy/Github/automation-sop-ajk-using-ansible/'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/start')
def start():
    command = "ansible-playbook -i %shosts %sservices.yml --tags 'start'" % ( home, home )
    print(command)
    subprocess.call(command, shell=True)
    return redirect('/')

@app.route('/restart')
def restart():
    command = "ansible-playbook -i %shosts %sservices.yml --tags 'restart'" % ( home, home )
    print(command)
    subprocess.call(command, shell=True)
    return redirect('/')

@app.route('/stop')
def stop():
    command = "ansible-playbook -i %shosts %sservices.yml --tags 'stop'" % ( home, home )
    print(command)
    subprocess.call(command, shell=True)
    return redirect('/')