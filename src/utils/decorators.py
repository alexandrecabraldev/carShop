from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from models.user import User
from models import Session

def user_role_validation(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        session = Session()
        current_user_id = get_jwt_identity()  
        current_user = session.query(User).filter_by(id=current_user_id).first()
        if not current_user or current_user.role != 'admin':
            session.close()
            return jsonify({
                "message": "Access forbidden: admin Only"
            }), 403
        session.close()
        return fun(*args, **kwargs)
    return wrapper