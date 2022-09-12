import os
from flask import redirect, url_for
from app import create_app

app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.route('/')
def home():
    return redirect(url_for('blueprint_v1.index', _external=True))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
