from sqlalchemy.orm import Session
import random, time

from app.models.beach import Beach
from app.schemas.beach import BeachCreate, BeachCondition


# ✅ Get all beaches from the database
def get_all_beaches(db: Session):
    return db.query(Beach).all()


# ✅ Create a new beach in the database
def create_beach(db: Session, beach_data: BeachCreate):
    beach = Beach(**beach_data.dict())
    db.add(beach)
    db.commit()
    db.refresh(beach)
    return beach


# ✅ Simulate safety_flag and timestamp for one beach record
def simulate_beach_data(beach: Beach) -> BeachCondition:
    return BeachCondition(
        id=beach.id,
        name=beach.name,
        wave_height=beach.wave_height,
        temperature=beach.temperature,
        crowd_level=beach.crowd_level,
        safety_flag=random.choice(["green", "yellow", "red"]),
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        regions=beach.regions,
        image_url=beach.image_url,
    )


# ✅ Return a list of BeachCondition objects (simulated)
def get_all_beaches_with_simulation(db: Session):
    beaches = get_all_beaches(db)
    return [simulate_beach_data(beach) for beach in beaches]

def get_beaches_by_crowd_level(db: Session, crowd_level: str):
    return db.query(Beach).filter(Beach.crowd_level == crowd_level).all()

