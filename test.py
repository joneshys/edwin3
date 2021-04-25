import boto3
from flask import Flask, request, jsonify
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ast

app = Flask(__name__)

@app.route('/')
def hello_wold():
    return 'Hola mundo, desde un docker que se encuentra en AWS'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)