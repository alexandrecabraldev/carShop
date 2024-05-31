from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt
from models.user import User
from models import Session
from schemas.user_schema import UserInputBodySchema

user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()

user_validate = UserInputBodySchema()

@user_bp.route('/user', methods=['POST'])
def create_user():
    session = Session()
    user_valid = user_validate.load(request.get_json())
    hashed_password = bcrypt.generate_password_hash(user_valid['password']).decode('utf-8')
    new_user = User(
        username=user_valid['username'],
        email=user_valid['email'],
        password=hashed_password,
        role=user_valid['role']
    )
    try:
        session.add(new_user)
        session.commit()
        session.close()
        return jsonify({"message": "user created"}), 201
    
    except Exception as e:
        session.rollback()
        session.close()
        return jsonify({"message": str(e)}), 400

@user_bp.route('/login', methods=['POST'])
def login():

    session = Session()
    email = request.json.get('email')
    password = request.json.get('password')

    user = session.query(User).filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        session.close()
        return jsonify({"message": "invalid credentials"}), 404
    
    token = create_access_token(identity=user.id)
    session.close()

    return jsonify({"token": token}), 200