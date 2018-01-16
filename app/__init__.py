# app/__init__.py
from flask import request, jsonify, abort
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config



# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Alert
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/alerts/', methods=['POST', 'GET'])
    def alerts():
        if request.method == "POST":
            title = str(request.data.get('title', ''))
            message = str(request.data.get('message', ''))
            if title and message:
                alert = Alert(title=title, message=message)
                alert.save()
                response = jsonify({
                    'id': alert.id,
                    'title': alert.title,
                    'message': alert.message,
                    'date_created': alert.date_created,
                    'date_modified': alert.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            alerts = Alert.get_all()
            results = []

            for alert in alerts:
                obj = {
                    'id': alert.id,
                    'title': alert.title,
                    'message': alert.message,
                    'date_created': alert.date_created,
                    'date_modified': alert.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/alerts/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def alert_manipulation(id, **kwargs):
     # retrieve a buckelist using it's ID
        alert = Alert.query.filter_by(id=id).first()
        if not alert:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            alert.delete()
            return {
            "message": "alert {} deleted successfully".format(alert.id) 
        }, 200
        elif request.method == 'PUT':
            message = str(request.data.get('message', ''))
            title = str(request.data.get('title', ''))
            if title == "" and message == "":
                return {"message": "Alert needs title or message to be filled in"}, 500
            alert.title = title
            alert.message = message
            alert.save()
            response = jsonify({
                'id': alert.id,
                'title': alert.title,
                'message': alert.message,
                'date_created': alert.date_created,
                'date_modified': alert.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': alert.id,
                'title': alert.title,
                'message': alert.message,
                'date_created': alert.date_created,
                'date_modified': alert.date_modified
            })
            response.status_code = 200
            return response


    return app