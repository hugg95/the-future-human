from frontend import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lncwwn@localhost/lncwwn'
db = SQLAlchemy(app)
