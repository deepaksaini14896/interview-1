from sqlalchemy.orm import Session

from . import models,schemas


def get_address(db: Session, lat: float, lng: float):
    return db.query(models.GPS).filter(models.GPS.lat == lat, models.GPS.lng == lng).first()


def check_coordinates(db: Session, pincode: str, address: str, city: str, lat: float, lng: float):
	if db.query(models.GPS).filter(models.GPS.pincode == pincode).first():
		return True
	elif db.query(models.GPS).filter(models.GPS.lat == lat, models.GPS.lng == lng).first():
		return True
	return False


def create_coordinates(db: Session, pincode: str, address: str, city: str, lat: float, lng: float):
    db_user = models.GPS(pincode=pincode, address=address, city=city, lat=lat, lng=lng)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user