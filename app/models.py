# coding: utf-8
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ShortUrl(Base):
    __tablename__ = 'short_url'

    id = Column(BIGINT(20), primary_key=True)
    short_url = Column(String(255), nullable=False, server_default=text("''"))
    original_url = Column(String(255), nullable=False, server_default=text("''"))
    createdTime = Column(DateTime, nullable=False)
    updatedTime = Column(DateTime, nullable=False)
    removedTime = Column(DateTime, nullable=False)
