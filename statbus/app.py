from flask import Flask, render_template, request
from playhouse.flask_utils import FlaskDB


from statbus.database import db_wrapper
from statbus.cache import cache
from statbus.views import home, polls


def create_app(test_config=None):

	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	if test_config:
		app.config.update(test_config)
	cache.init_app(app)
	db_wrapper.init_app(app)


	# Blueprints
	app.register_blueprint(home.bp)
	app.register_blueprint(polls.bp)


	# Generic handler
	@app.errorhandler(403)
	@app.errorhandler(404)
	@app.errorhandler(500)
	def internal_error(e):
		return render_template('error.html', error=e), e.code

	return app