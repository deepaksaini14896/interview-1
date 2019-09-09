from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:  
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.post("/post_location/{pincode}&{address}&{city}&{lat}&{lng}", response_model=schemas.UserBase)
def create_user(pincode: str, address: str, city: str, lat: float, lng: float, db: Session = Depends(get_db)):
    db_user = crud.check_coordinates(db, pincode=pincode, address=address, city=city, lat=lat, lng=lng)
    if db_user:
        raise HTTPException(status_code=400, detail="Don't assume that they will exactly be the same.")
    return crud.create_coordinates(db=db, pincode=pincode, address=address, city=city, lat=lat, lng=lng)


@app.get("/get_location/{lat}&{lng}", response_model=schemas.CityCreate)
def read_user(lat: float, lng: float, db: Session = Depends(get_db)):
    db_user = crud.get_address(db, lat=lat, lng=lng)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Latitude and Longitude are not exist.")
    return db_user