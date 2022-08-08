import os
from flask import redirect, url_for
from app import create_app

app = create_app(os.environ.get('FLASK_DEBUG', 'development'))

@app.route('/')
def home():
    return redirect(url_for('blueprint_v1.index', _external=True))

if __name__ == '__main__':
    app.run(debug=True)
