from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import Config

Base = declarative_base()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)