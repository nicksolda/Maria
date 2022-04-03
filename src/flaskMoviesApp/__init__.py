from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_login import LoginManager

app = Flask(__name__)


### Configuration για τα Secret Key, WTF CSRF Secret Key, SQLAlchemy Database URL, 
## Το όνομα του αρχείου της βάσης δεδομένων θα πρέπει να είναι 'flask_movies_database.db'

app.config["SECRET_KEY"] = '2901c9483a12648404adc16d22b4b625'
app.config['WTF_CSRF_SECRET_KEY'] = 'fe9d487ba2c9a1f13a5d72fa0d'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_movies_database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


### Αρχικοποίηση της Βάσης, και άλλων εργαλείων ###
### Δώστε τις σωστές τιμές παρακάτω ###

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = "login_page"
login_manager.login_message_category = "warning"
login_manager.login_message = "Παρακαλούμε κάντε login για να μπορέσετε να δείτε αυτή τη σελίδα."


from flaskMoviesApp import routes, models