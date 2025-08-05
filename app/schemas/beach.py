from pydantic import BaseModel


# ✅ Shared base fields
class BeachBase(BaseModel):
    name: str
    temperature: float
    wave_height: float
    crowd_level: str
    safety_flag: str
    timestamp: str
    regions: str
    image_url: str 


# ✅ Schema for creating a beach (POST)
class BeachCreate(BeachBase):
    pass


# ✅ Schema for reading a beach from DB (GET one/all)
class BeachResponse(BeachBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 (use orm_mode in v1)


# ✅ If you still want a separate schema for simulation, you can use this:
class BeachCondition(BeachResponse):
    pass  # No difference unless you add simulated-specific fields
