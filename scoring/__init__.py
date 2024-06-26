import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'main_db.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import overview
    app.register_blueprint(overview.bp)

    from . import scorers
    app.register_blueprint(scorers.bp)
    app.add_url_rule('/', endpoint='index')

    # a simple page that tests if everything is working
    @app.route('/test')
    def test():
        return 'Hello, World!'

    return app
