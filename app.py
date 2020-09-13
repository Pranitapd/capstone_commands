import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

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

    if(len(all_commands) == 0):
      abort(404)

    return jsonify({
      'success': True,
      'all_commands':all_commands
    })

  @app.route('/commands/<int:category_id>')
  @requires_auth('get:categorised-commands')
  def get_categorised_commands(payload,category_id):
    commands_for_cat = Commands.query.filter(Commands.category == category_id)
    return jsonify({
      'success':True,
      'commands':commands_for_cat
    })

  @app.route('/categories')
  @requires_auth('get:categories')
  def get_categories(payload):
    cats = Category.query.all()
    return jsonify({
      'success':True,
      'categories':cats
    })

  @app.route('/commands', methods=['POST'])
  @requires_auth('post:commands')
  def add_commands(payload):
    try:
      body = request.get_json()
      command = body.get('command',None)
      category = body.get('category',None)
      explanation = body.get('explanation',None)

      new_command = Commands(command=command,category=category,explanation=explanation)
      new_command.insert()

      all_commands = Commands.query.all()

      return jsonify({
        'success':True,
        'new_command':new_command,
        'all_commands':all_commands
      })
    except:
      abort(405)


  @app.route('/commands/<int:command_id>',methods=['DELETE'])
  @requires_auth('delete:commands')
  def delete_command(jwt,command_id):
    command = Commands.query.filter(Commands.id == command_id)
    if not command:
      abort(404)

    command.delete()
    return jsonify({
      'success':True,
      'all_commands':Commands.query.all()
    })

  @app.route('/commands/<int:command_id>',methods=['PATCH'])
  @requires_auth('patch:commands')
  def alter_command(jwt,command_id):
    command = Command.query.get(command_id)
    if not command:
      abort(404)

    body = request.get_json()
    command = body.get('command',None)
    category = body.get('category',None)
    explanation = body.get('explanation',None)

    head = request.get_json(force=True)
    command.title = json.dumps(head.get('command'))
    command.category = json.dumps(head.get('category'))
    command.explanation = json.dumps(head.get('explanation'))
    command.update()

    return jsonify({
        'success':True,
        'updated_command' : Commands.query.get(command_id),
        'commands': Commands.query.all()
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
    return jsonify({
      'success':True,
      'all_suggestion':all_suggestions
    })

  @app.route('/suggestions')
  @requires_auth('get:suggestions')
  def get_suggestons(payload):
    suggestions = Suggestion.query.all()
    return jsonify({
      'success':True,
      'suggestions':suggestions
    })

  @app.route('/suggestions/<int:sug_id>',methods=['DELETE'])
  @requires_auth('delete:suggestions')
  def delete_suggestions(jwt,sug_id):
    sug = Suggestion.query.get(sug_id)
    sug.delete()

    return jsonify({
      'success':True,
      'suggestions':Suggestion.query.all()
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

  return app

APP = create_app()



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)