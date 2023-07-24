from sqlalchemy import Column, Integer, String
from scraper.base import DeclarativeBase


class Estates(DeclarativeBase):

    __tablename__ = "estates"

    id = Column(Integer, primary_key=True)
    title = Column("title", String)
    imgURL = Column("imgURL", String)