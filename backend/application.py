from flask import Flask
from app import application

if __name__=="__main__":
    application.run(debug=True,use_reloader=False)
