import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json
from flask_migrate import Migrate
from models import db,Commands,Suggestion,Category,setup_db

#print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
from auth.auth import requires_auth,AuthError

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  CORS(app, resources={r"/api/*": {"origins": "*"}})
  app.config['CORS_HEADERS'] = 'Content-Type'

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH')
    return response

  @app.route('/commands/')
  @cross_origin()
  def get_commands():
    all_commands = Commands.query.all()
    commands_formatted = [ command.format() for command in all_commands ]

    if(len(all_commands) == 0):
      abort(404)

    return jsonify({
      'success': True,
      'all_commands':commands_formatted
    })

  @app.route('/commands/<int:category_id>')
  @requires_auth('get:categorised-commands')
  def get_categorised_commands(payload,category_id):
    commands_for_cat = Commands.query.filter(Commands.category == category_id).all()
    if(len(commands_for_cat) == 0):
      abort(404)
    commands_formatted = [ command.format() for command in commands_for_cat ]
    return jsonify({
      'success':True,
      'commands':commands_formatted
    })

  @app.route('/categories')
  @requires_auth('get:categories')
  def get_categories(payload):
    cats = Category.query.all()
    formatted_categories = [ cat.format() for cat in cats ]
    return jsonify({
      'success':True,
      'categories':formatted_categories
    })

  @app.route('/commands', methods=['POST'])
  @requires_auth('post:commands')
  def add_commands(payload):
    try:
      #body = request.get_json()
      command = request.json.get('command')
      category = request.json.get('category')
      explanation = request.json.get('explanation')

      if command is None or category is None or explanation is None:
        abort(400)

      new_command = Commands(command=command,category=category,explanation=explanation)
      new_command.insert()

      all_commands = Commands.query.all()
      formatted_command = [ comma.format() for comma in all_commands ]

      return jsonify({
        'success':True,
        'new_command':new_command.format(),
        'all_commands':formatted_command
      })
    except:
      abort(405)


  @app.route('/commands/<int:command_id>',methods=['DELETE'])
  @requires_auth('delete:commands')
  def delete_command(jwt,command_id):
    command = Commands.query.filter(Commands.id == command_id).first()
    if not command:
      abort(404)

    command.delete()
    all_commands = Commands.query.all()
    formatted_command = [ comma.format() for comma in all_commands ]

    command.delete()
    return jsonify({
      'success':True,
      'all_commands':formatted_command
    })

  @app.route('/commands/<int:command_id>',methods=['PATCH'])
  @requires_auth('patch:commands')
  def alter_command(jwt,command_id):
    comm = Commands.query.filter(Commands.id == command_id).first()
    if not comm:
      abort(404)

    body = request.get_json(force=True)
    comm.command = json.dumps(body.get('command', comm.command))
    comm.category = json.dumps(body.get('category', comm.category))
    comm.explanation = json.dumps(body.get('explanation', comm.explanation))

    comm.update()

    all_commands = Commands.query.all()
    formatted_command = [ comma.format() for comma in all_commands ]

    return jsonify({
        'success':True,
        'updated_command' : Commands.query.get(command_id).format(),
        'commands': formatted_command
    })

  @app.route('/suggestions',methods=['POST'])
  @requires_auth('add:suggestions')
  def add_suggestions(payload):
    body = request.get_json()
    suggestion = body.get('suggestion',None)
    category = body.get('category',None)

    new_sug= Suggestion(suggestion=suggestion,category=category)
    new_sug.insert()

    all_suggestions = Suggestion.query.all()
    formatted_sugg = [ sug.format() for sug in all_suggestions ]
    return jsonify({
      'success':True,
      'all_suggestion':formatted_sugg
    })

  @app.route('/suggestions')
  @requires_auth('get:suggestions')
  def get_suggestons(payload):
    suggestions = Suggestion.query.all()
    formatted_sugg = [ sug.format() for sug in suggestions ]
    return jsonify({
      'success':True,
      'suggestions':formatted_sugg
    })

  @app.route('/suggestions/<int:sug_id>',methods=['DELETE'])
  @requires_auth('delete:suggestions')
  def delete_suggestions(jwt,sug_id):
    suggestions = Suggestion.query.filter(Suggestion.id == sug_id).first()
    if not suggestions:
      abort(404)
    suggestions.delete()
    all_suggestion = Suggestion.query.all()
    formatted_sugg = [ sug.format() for sug in all_suggestion ]
    return jsonify({
      'success':True,
      'suggestions':formatted_sugg
    })

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success":False,
        "error":404,
        "message":"resource not found"
    }), 404

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
        "success":False,
        "error":405,
        "message":"method not allowed"
    })
  
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400

  return app

APP = create_app()



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)