from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import json

USERS = {
    "admin":"admin_mobile",
    "user_test":"test_password"
}

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-mega-ultra-secret-key"
jwt = JWTManager(app)

@app.route("/", methods=['GET'])
def callback():
    return jsonify({"msg":"API is ALIVE."})

@app.route("/login", methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"msg":"Credentials missing."}), 400

    if username not in USERS.keys() or password != USERS[username]:
        return jsonify({"msg":"Bad username or password."}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/tree', methods=['GET', 'POST'])
@jwt_required()
def tree():
    if request.method == 'GET':
        with open("arvore_teste.json", 'r') as file:
            data = json.load(file)
        return jsonify(data)
    
    elif request.method == 'POST':
        id = request.json.get("id", None)
        name = request.json.get("name", None)

        if not id or not name:
            return jsonify({"msg":"Missing parameters."}), 400
        
        with open("arvore_teste.json", 'r') as file:
            data = json.load(file)

        for item in data:
            if item['id'] == id:
                item['name'] = name.strip().upper()
                break

        with open("arvore_teste.json", 'w') as file:
            json.dump(data, file, indent=4)

        return jsonify({"msg": "Node updated successfully."}), 200

if __name__ == "__main__":
    app.run()