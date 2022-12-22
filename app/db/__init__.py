from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

#Here we connect to the DB using or env
#The engine variable manages our connection to the DB
#The Session variable generates temp connection for CRUD operations
#The base variable assists in mapping the models to SQL tables
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()