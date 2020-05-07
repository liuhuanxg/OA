#-*-coding:utf-8 -*-
"""
@project:OA
@File: settings.py.py
@user：liuhuan   
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///OA.sqlite"
# 链接mysql时设置：mysql://username:password@server/db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)