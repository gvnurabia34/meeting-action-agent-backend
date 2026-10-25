
from datetime import datetime
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Meeting

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Meeting Action Agent API")


class MeetingCreate(BaseModel):
    title: str = Field(..., min_length=1)
    meeting_at: Optional[datetime] = None


class MeetingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    meeting_at: Optional[datetime] = None
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post(
    "/api/v1/meetings",
    response_model=MeetingResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_meeting(
    meeting_data: MeetingCreate,
    db: Session = Depends(get_db),
):
    meeting = Meeting(
        title=meeting_data.title,
        meeting_at=meeting_data.meeting_at,
    )

    db.add(meeting)
    db.commit()
    db.refresh(meeting)

    return meeting


@app.get("/api/v1/meetings", response_model=list[MeetingResponse])
def list_meetings(db: Session = Depends(get_db)):
    return db.query(Meeting).order_by(Meeting.created_at.desc()).all()


@app.get("/api/v1/meetings/{meeting_id}", response_model=MeetingResponse)
def get_meeting(meeting_id: str, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()

    if meeting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meeting not found",
        )

    return meeting
