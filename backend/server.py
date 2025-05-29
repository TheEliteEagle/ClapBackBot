from flask import Flask, jsonify, request
from flask_cors import CORS
from generate_response import generate


server = Flask(__name__)
CORS(server)

@server.route('/comeback', methods=["POST"])
def handle_comeback():
    
    comeback = generate(request.get_json()['roast'])

    return jsonify({'comeback': comeback})

if __name__ == '__main__':
    server.run(host='localhost', port=5000)