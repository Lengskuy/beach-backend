from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.beach import BeachCreate, BeachResponse, BeachCondition
from app.database.connection import SessionLocal
from app.services import beach_service
from fastapi import Query
import random
import time

router = APIRouter()

# ✅ Function to simulate dynamic data
def simulate_beach_data():
    base_beaches = [
        {
            "id": 1,
            "name": "Pantai Merdeka",
            "temperature": 30.0,
            "wave_height": 1.0,
            "crowd_level": "Low",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "North",
            "image_url": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4nqkjtlBxAHY1TAqS-U5h1HzExKTWLVe93l355sIG0PvtA3O0genjcBJmKyI1ygZGkePbOuL8OdOa5ixkLNtvLsSW3vAZ2um8a0oPhDvuYcbzhHWnKYOogrfI_fOufi-SgpydBWx=s1360-w1360-h1020-rw"
        },
        {
            "id": 2,
            "name": "Pantai Cahaya Bulan",
            "temperature": 32.0,
            "wave_height": 1.8,
            "crowd_level": "Medium",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "East",
            "image_url": "https://www.caridestinasi.com/wp-content/uploads/2015/08/berkelah-di-pantai-cahaya-bulan.jpg"
        },
        {
            "id": 3,
            "name": "Pantai Bagan Lalang",
            "temperature": 28.0,
            "wave_height": 1.0,
            "crowd_level": "Low",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "West",
            "image_url": "https://www.caridestinasi.com/wp-content/uploads/2015/08/percutian-ke-resort-avani-bagan-lalang.png"
        },
        {
            "id": 4,
            "name": "Pantai Kuala Perlis",
            "temperature": 28.0,
            "wave_height": 0.9,
            "crowd_level": "Low",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "North",
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd907ygV7-It-omT-1RNng7XV5y7OWiLK6hg&s"
        },
        {
            "id": 5,
            "name": "Pantai Batu Burok",
            "temperature": 31.0,
            "wave_height": 1.6,
            "crowd_level": "Medium",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "East",
            "image_url": "https://www.discoveryterengganu.com/wp-content/uploads/2024/04/1-23.jpg"
        },
        {
            "id": 6,
            "name": "Pantai Redang",
            "temperature": 30.0,
            "wave_height": 1.1,
            "crowd_level": "Medium",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "West",
            "image_url": "https://www.holidaygogogo.com/wp-content/uploads/2020/08/Environment-1-1.jpg"
        },
    ]

    dynamic_data = []
    for beach in base_beaches:
        dynamic_data.append({
            **beach,
            "temperature": round(random.uniform(27.0, 34.0), 1),
            "wave_height": round(random.uniform(0.5, 2.5), 1),
            "crowd_level": random.choice(["Low", "Medium", "High"]),
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    return dynamic_data

# ✅ Route that returns dynamic mocked beach data
@router.get("/mock", response_model=List[BeachCondition])
def get_mocked_beaches():
    return simulate_beach_data()
