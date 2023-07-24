from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine

from scraper import settings


DeclarativeBase = declarative_base()


def db_connect() -> Engine:

    return create_engine(URL.create(**settings.DATABASE))


def create_estates_table(engine: Engine):

    DeclarativeBase.metadata.create_all(engine)