from flask import Flask, render_template

from controllers.parks_controller import parks_blueprint
from controllers.lands_controller import lands_blueprint
from controllers.attractions_controller import attractions_blueprint

app = Flask(__name__)

app.register_blueprint(parks_blueprint)
app.register_blueprint(lands_blueprint)
app.register_blueprint(attractions_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

