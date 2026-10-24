from app.database import Base, engine, SessionLocal
from app import models

Base.metadata.create_all(bind=engine)

db = SessionLocal()
m = models.Meeting(title="Örnek Toplantı")
db.add(m)
db.commit()
db.refresh(m)
print("Kaydedildi:", m.id, m.title, m.status)

okunan = db.query(models.Meeting).filter(models.Meeting.id == m.id).first()
print("Okundu:", okunan.title)
db.close()