from datetime import datetime
import uuid

from typing import TYPE_CHECKING, List
from sqlmodel import Field, SQLModel

from app.schemas.comments import CommentRead
from app.schemas.like import LikeRead

if TYPE_CHECKING:
    from app.schemas.like import LikeRead
    from app.schemas.comments import CommentRead
    from app.schemas.images import ImageRead
    
class PostCreate(SQLModel):
    description: str
    user_id: uuid.UUID


class PostRead(SQLModel):
    id: uuid.UUID
    user_id: uuid.UUID
    description: str
    created_at: datetime
    images: List["ImageRead"] = Field(default_factory=list)
    likes_count: int = 0
    comments_count: int = 0

class PostReadDetails(SQLModel):
    id: uuid.UUID
    user_id: uuid.UUID
    description: str
    created_at: datetime
    images: List["ImageRead"] = Field(default_factory=list)

    likes: List["LikeRead"] = Field(default_factory=list)
    comments: List["CommentRead"] = Field(default_factory=list)

from app.schemas.images import ImageRead
from app.schemas.like import LikeRead
from app.schemas.comments import CommentRead

PostReadDetails.model_rebuild()
PostRead.model_rebuild()

class PostUpdate(SQLModel):
    description: str | None = None
    user_id: uuid.UUID | None = None