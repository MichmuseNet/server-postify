from datetime import datetime
import uuid
from sqlmodel import SQLModel

class ImageRead(SQLModel):
    id: uuid.UUID
    url: str
    public_id: str
    post_id: uuid.UUID
    created_at: datetime | None = None
