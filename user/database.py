from fastapi import FastAPI, HTTPException, Depends,status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from sqlalchemy.orm import Session

# breakpoint() 

URL_DATABASE = "postgresql://competitionuser:YdfWB4R9xpgfnXx8qKlfHhTvcve5VDRV@dpg-ctvrhorv2p9s7398d650-a.oregon-postgres.render.com/competition_ftzg"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
