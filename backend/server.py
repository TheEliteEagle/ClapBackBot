from flask import Flask, jsonify, request
from generate_response import generate


server = Flask(__name__)

@server.route('/comeback', methods=["POST"])
def handle_comeback():
    
    comeback = generate(request.form['roast'])
    
    return jsonify({'comeback': comeback})

if __name__ == '__main__':
    server.run(host='localhost', port=5000)