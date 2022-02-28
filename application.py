from flask import Flask  # From 'flask' module import 'Flask' class
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(_name_)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler (or view function)
def main():

    return f'ATC_USERNAME={os.getenv("ATC_USERNAME")},ATC_PASSWORD={os.getenv("ATC_PASSWORD")}'

if _name_ == '_main_':  # Script executed directly (instead of via import)?
    app.run(host="0.0.0.0")  # Launch built-in web server and run this Flask webapp