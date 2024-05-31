from controllers.car_controller import car_bp
from controllers.user_controller import user_bp

def register_controllers(app):
    app.register_blueprint(car_bp)
    app.register_blueprint(user_bp)