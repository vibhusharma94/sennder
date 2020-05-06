from http import HTTPStatus
from flask import render_template, make_response
from flask_restful import Resource


class HomeController(Resource):

    def get(self):
        """
        Entry point to site.
        :return: render html page
        """
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), HTTPStatus.OK, headers)
