# 即控制器（Controller）- 
# 對 Request/Response 進行處理並透過 Controller 
# 把 Model 的資料串接到 View（Templates）
# SQLAlchemy 是 Python 社群最廣泛使用的 ORM(不同類型系統的資料之間的轉換) 套件
import os

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# initialize
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import views
