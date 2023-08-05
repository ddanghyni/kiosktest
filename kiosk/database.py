from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('/Users/ddanghyni0425/kiosktest/kiosk')
import json

SECRET_FILE = '/Users/ddanghyni0425/kiosktest/kiosk/secrets.json'

with open(SECRET_FILE, 'r') as f:
    secrets = json.load(f)

DB = secrets['DB']

DB_URL = f"mysql+pymysql://{DB['USER']}:{DB['PASSWORD']}@{DB['HOST']}:{DB['PORT']}/{DB['NAME']}?charset=utf8"

engine = create_engine(
    DB_URL
)

SessionLocal = sessionmaker(autocommit=False, 
                            autoflush=False, 
                            bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

