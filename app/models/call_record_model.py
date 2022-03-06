from app.configs.database import db
from sqlalchemy import Column, Integer, String, Date, DateTime
from dataclasses import dataclass

@dataclass
class CallRecord(db.Model):
    id: int
    source: int
    destination: str
    start_time: str
    end_time: str

    __tablename__ = 'call_records'

    id = Column (Integer, primary_key = True)
    source = Column(Integer, nullable=False)
    destination = Column(String, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # Function for serializer while dataclass off 
    def serializer(self):
        return {"id":self.id, "source":self.source, 
        "destination":self.destination, "start_time":self.start_time, "end_time": self.end_time}