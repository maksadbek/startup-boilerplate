db:
	FLASK_APP=app.main poetry run flask db

run:
	FLASK_DEBUG=1 FLASK_APP=app.main poetry run flask run
