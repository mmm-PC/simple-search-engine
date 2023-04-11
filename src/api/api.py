import os
import json
from flask import Flask, Response, jsonify, abort, render_template, request, redirect, send_from_directory, url_for
from src.config.cfg_parser import get_config


class API:
    def __init__(self, database, index):
        config = get_config('config.ini')
        server_cfg = config['server']

        self.database = database
        self.index = index
        self.app = Flask(__name__)

        @self.app.errorhandler(404)
        def resource_not_found(e):
            return jsonify(error=str(e)), 404

        @self.app.route('/')
        def homepage():
            return redirect("/search", code=302)

        @self.app.route('/api/search', methods=['GET'])
        def search():
            query = request.args.get("q", default="", type=str)
            results = self.index.search(
                query, size=20, source=True, source_includes=['id'])

            result = []
            for res in results:
                result.append(self.database.get_by_id(res['id']))

            return jsonify(result)

        @self.app.route('/api/delete/<id>', methods=['DELETE'])
        def delete(id):
            try:
                self.index.delete_by_id(id)
                self.database.delete_by_id(id)

                return Response(response="{'message':'success'}", status=200, mimetype='application/json')
            except:
                return Response(response="{'message':'error'}", status=404, mimetype='application/json')

        @self.app.route('/search')
        def search_front():
            return send_from_directory('..\\..\\web\\html', 'search.html')
