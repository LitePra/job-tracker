from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Job(Base):
    __tablename__ = "jobs"

    