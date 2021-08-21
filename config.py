#configurações basicas para a funcionalidade do programa
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
caminho =  os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho, "aprovei.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICTIONS'] = False
db = SQLAlchemy(app)
