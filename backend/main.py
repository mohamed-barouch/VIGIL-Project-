from datetime import datetime
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from db import engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vigil")


def get_db():
    with Session(engine) as session:
        yield session


class EventIn(BaseModel):
    ts: datetime
    method: str
    path: str
    status: int
    latency_ms: int
    ip: str | None = None
    error_text: str | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/v1/events", status_code=201)
def create_event(event: EventIn, db: Session = Depends(get_db)):
    row = models.Event(**event.model_dump())
    db.add(row)
    db.commit()
    return {"id": row.id}


@app.get("/v1/events")
def list_events(limit: int = 100, db: Session = Depends(get_db)):
    rows = db.scalars(
        select(models.Event).order_by(models.Event.ts.desc()).limit(limit)
    ).all()
    return [
        {"id": r.id, "ts": r.ts, "method": r.method, "path": r.path,
         "status": r.status, "latency_ms": r.latency_ms,
         "ip": r.ip, "error_text": r.error_text}
        for r in rows
    ]