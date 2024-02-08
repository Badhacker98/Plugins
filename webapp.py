from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def start():
    return "PbxBot Started Successfully"

os.system("python3 -m TelethonPbx")
app.run(port=5000)
