from sqlalchemy.orm import Mapped,mapped_column
from .base import Base

class JobORM(Base):
    __tablename__ = "jobs"

    title: Mapped[str] = mapped_column()
    stack: Mapped[str]
    experience: Mapped[int] = mapped_column(default=0)
    apply: Mapped[bool] = mapped_column(default=False)