from flask.cli import FlaskGroup

from green_gate.api import app


cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
