from datetime import timedelta

class Config:
    JWT_SECRET_KEY= 'fakjlhsncgfdansawknçhjcdfcja'
    JWT_ACESS_TOKEN_EXPIRES = timedelta(hours=1)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:admin@localhost/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
