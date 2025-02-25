from flask import Flask,jsonify
from src.routes import blueprints  # Import the blueprints list
from src.utils.helpers import format_response_success, format_response_fail


def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

    # Register each Blueprint in the blueprints list
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    
    @app.errorhandler(413)
    def request_entity_too_large(error):
        return (format_response_fail("413", "File is too large. The maximum file size is 100 MB")), 413


    return app
