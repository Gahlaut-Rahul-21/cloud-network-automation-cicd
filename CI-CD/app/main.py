"""Flask API exposing network automation helpers."""

import os

from flask import Flask, jsonify, request

from app import netutils

__version__ = "1.0.0"


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=os.getenv("APP_VERSION", __version__))

    @app.get("/subnet")
    def subnet():
        cidr = request.args.get("cidr", "")
        try:
            return jsonify(netutils.subnet_info(cidr))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

    @app.get("/overlap")
    def overlap():
        a, b = request.args.get("a", ""), request.args.get("b", "")
        try:
            return jsonify(a=a, b=b, overlap=netutils.cidrs_overlap(a, b))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

    @app.get("/split")
    def split():
        cidr = request.args.get("cidr", "")
        try:
            prefix = int(request.args.get("prefix", ""))
            return jsonify(subnets=netutils.split_subnet(cidr, prefix))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

    return app


app = create_app()
