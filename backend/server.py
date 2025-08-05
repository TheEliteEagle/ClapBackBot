from flask import Flask, jsonify, request
from flask_cors import CORS
from generate_response import generate, generate_lite
import os
from dotenv import load_dotenv
load_dotenv(".env.local")

# set mode of server
BACKEND_MODE = os.getenv("BACKEND_MODE", "normal")
generate_call = generate_lite if BACKEND_MODE == "lite" else generate

server = Flask(__name__)
CORS(server)

@server.route('/comeback', methods=["POST"])
def handle_comeback():
    
    comeback = generate_call(request.get_json()['roast'])

    return jsonify({'comeback': comeback})

if __name__ == '__main__':
    print(f"\nStarted server in {BACKEND_MODE} mode\n")
    server.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))  