from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from config import Config
from models import Base, engine
from controllers import register_controllers

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
ma = Marshmallow(app)
CORS(app)

Base.metadata.create_all(engine)

register_controllers(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# import uuid
# from sqlalchemy.dialects.postgresql import UUID
# from flask import Flask, request, jsonify 
# from marshmallow import fields
# from flask_marshmallow import Marshmallow
# from sqlalchemy import create_engine, Column,String
# from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy_utils import URLType
# from flask_jwt_extended import jwt_required, JWTManager, create_access_token, get_jwt_identity
# from flask_bcrypt import Bcrypt
# from functools import wraps
# from datetime import timedelta
# from flask_cors import CORS    

# app = Flask(__name__)
# ma = Marshmallow(app)
# app.config['JWT_SECRET_KEY'] = 'fakjlhsncgfdansawknçhjcdfcja'
# app.config['JWT_ACESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# jwt = JWTManager(app)
# bcrypt = Bcrypt(app)
# engine = create_engine('postgresql+psycopg2://admin:admin@localhost/database')

# CORS(app)

# Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()

# class Car(Base):
#     __tablename__= 'cars'
#     id=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name=Column(String(50), nullable=False)
#     brand=Column(String(50), nullable=False)
#     model=Column(String(50), nullable=False)
#     image_url=Column(URLType, nullable=False)

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "brand": self.brand,
#             "model": self.model,
#             "image_url": self.image_url
#         }
    
#     def __repr__(self):
#         return f"id={self.id}, name={self.name}, brand={self.brand}, model={self.model}, image_url={self.image_url}"
    
# class User(Base):
#     __tablename__='users'
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     username = Column(String(50), nullable=False)
#     email = Column(String(50), unique=True, nullable=False)
#     password = Column(String(150), nullable=False)
#     role = Column(String(50), default='customer')

# Base.metadata.create_all(engine)

# class CarInputBodySchema(ma.Schema):
#     name= fields.String(required=True)
#     brand= fields.String(required=True)
#     model= fields.String(required=True)
#     image_url= fields.URL(required=True)

# class UserInputBodySchema(ma.Schema):
#     username = fields.String(required=True)
#     email = fields.Email(required=True)
#     password = fields.String(required=True)
#     role= fields.String()

# class CarUpdateBodySchema(ma.Schema):
#     name= fields.String()
#     brand= fields.String()
#     model= fields.String()
#     image_url= fields.URL()

# car_validate = CarInputBodySchema()
# car_update_validate = CarUpdateBodySchema()
# user_validate = UserInputBodySchema()


# def user_role_validation(fun):
#     @wraps(fun)
#     def wrapper(*args, **kwargs):
#         current_user_id = get_jwt_identity()  
#         current_user = session.query(User).filter_by(id=current_user_id).first()

#         if not current_user or current_user.role != 'admin':
#             return jsonify({
#                 "message": "Acess forbidden: admin Only"
#             }), 403
#         return fun(*args, **kwargs)
#     return wrapper


# @app.route('/user', methods=['POST'])
# def create_user():
    
#     print('passou aqui')
#     user_valid = user_validate.load(request.get_json())
#     hashed_password = bcrypt.generate_password_hash(user_valid['password']).decode('utf-8')
    
#     if 'role' in user_valid:
#         new_user = User(
#         username = user_valid['username'],
#         email = user_valid['email'],
#         password = hashed_password,
#         role = user_valid['role']
#     )
#     else:
#         new_user = User(
#         username = user_valid['username'],
#         email = user_valid['email'],
#         password = hashed_password
#     )
    
    
#     try:
#         print('entrou aqui')
#         session.add(new_user)
#         session.commit()
#         return jsonify({"message": "user created"}),201
#     except Exception as e:
#         session.rollback()
#         return jsonify({"message": str(e)}), 400
    

# @app.route('/login', methods=['POST'])
# def login():
#     email = request.json.get('email')
#     password = request.json.get('password')
    
#     user = session.query(User).filter_by(email=email).first()

#     if not user:
#         return jsonify({
#             "message": "invalid credentials"
#         }), 404

#     isPasswordValid = bcrypt.check_password_hash(user.password, password)

#     if not isPasswordValid:
#         return jsonify({
#             "message": "invalid credentials"
#         }), 404

#     token = create_access_token(identity=user.id)

#     return jsonify({
#         "token": token
#     })

# @app.route('/car', methods=['GET'])
# def get_all_cars():
#     cars_list = session.query(Car).all()

#     car_list_dict = [Car.to_dict() for Car in cars_list]

#     return jsonify(
#         car_list_dict
#     )

# @app.route('/car', methods=['POST'])
# @jwt_required()
# @user_role_validation
# def create_cars():
#     # name, brand, model, image-url
#     car_data = request.get_json()
#     validated_car = car_validate.load(car_data)
#     print(validated_car['name'])

#     new_car = Car(
#         name=validated_car['name'],
#         brand=validated_car['brand'],
#         model=validated_car['model'],
#         image_url=validated_car['image_url']
#     )

#     session.add(new_car)
#     session.commit()

#     return jsonify({"data": new_car.name})

 
# @app.route('/car/<string:car_id>', methods=['PUT'])
# @jwt_required()
# @user_role_validation
# def update_car(car_id): 

#     try:
#         car_data = request.get_json()
#         car_valid = car_update_validate.load(car_data)  

#         car = session.query(Car).filter_by(id=car_id).first()

#         if not car:
#             return jsonify({
#                 "message": "Car not found"
#             })
         
#         for key, value in car_valid.items():
#             setattr(car,key,value)
        
#         session.commit()

#         return jsonify({"message": "update car"}), 200     
#     except Exception as e:
#         session.rollback()
#         return jsonify({
#             "message": str(e)
#         }), 400
         
     

# @app.route('/car/<string:car_id>', methods=['DELETE'])
# @jwt_required()
# @user_role_validation
# def delete_car(car_id):
#     try:
#         car = session.query(Car).filter_by(id=car_id).first()

#         if not car:
#             return jsonify({
#                 "message": "Car not found!!!"
#             }), 404
        
#         session.delete(car)
#         session.commit()

#         return jsonify({
#             "message": "car Deleted sucessfull"
#         }), 200
#     except Exception as e:
#         session.rollback()

#         return jsonify({
#             "message": str(e)
#         }), 400


# if __name__ =='__main__':
#     app.run(debug=True, port=5000)
