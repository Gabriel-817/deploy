#  서비스
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'aws 홈페이지'

if __name__ == '__maim__':
    app.run( debug=True )