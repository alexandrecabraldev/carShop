from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.car import Car
from models import Session
from schemas.car_schema import CarInputBodySchema, CarUpdateBodySchema
from utils.decorators import user_role_validation

car_bp = Blueprint('car_bp', __name__)

car_validate = CarInputBodySchema()
car_update_validate = CarUpdateBodySchema()

@car_bp.route('/car', methods=['GET'])
def get_all_cars():
    session = Session()
    cars_list = session.query(Car).all()
    car_list_dict = [car.to_dict() for car in cars_list]
    session.close()
    return jsonify(car_list_dict)

@car_bp.route('/car', methods=['POST'])
@jwt_required()
@user_role_validation
def create_cars():

    session = Session()
    car_data = request.get_json()
    validated_car = car_validate.load(car_data)

    new_car = Car(
        name=validated_car['name'],
        brand=validated_car['brand'],
        model=validated_car['model'],
        price=validated_car['price'],
        image_url=validated_car['image_url']
    )
    data= new_car.to_dict()

    try:
        session.add(new_car)
        session.commit()
        session.close()
        return jsonify({"data": data['name']}), 201
    except Exception as e:
        session.rollback()
        session.close()
        return jsonify({"message": str(e)}), 400

@car_bp.route('/car/<string:car_id>', methods=['PUT'])
@jwt_required()
@user_role_validation
def update_car(car_id):
    
    print('passou aqui')
    session = Session()
    car_data = request.get_json()

    car_valid = car_update_validate.load(car_data)

    car = session.query(Car).filter_by(id=car_id).first()
    
    if not car:
        session.close()
        return jsonify({"message": "Car not found"})
    
    for key, value in car_valid.items():
        setattr(car, key, value)
    session.commit()
    session.close()
    return jsonify({"message": "update car"}), 200

@car_bp.route('/car/<string:car_id>', methods=['DELETE'])
@jwt_required()
@user_role_validation
def delete_car(car_id):
    session = Session()
    car = session.query(Car).filter_by(id=car_id).first()
    if not car:
        session.close()
        return jsonify({"message": "Car not found"}), 404
    session.delete(car)
    session.commit()
    session.close()
    return jsonify({"message": "car Deleted successful"}), 200