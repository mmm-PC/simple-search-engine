from flask import Flask, jsonify
# from src.config.cfg_parser import get_config

app = Flask(__name__)

@app.route('/')
def homepage():
    return jsonify({'id': 'id'})