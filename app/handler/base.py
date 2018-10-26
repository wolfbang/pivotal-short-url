#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : base.py
# @Author: lucas
# @Date  : 10/1/18
# @Desc  :


from app.models import ShortUrl
from app.handler import utils
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import logging

reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(filename='pivotal-short-url.log', filemode='wb',
                    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# create models with sqlacodegem
# sqlacodegen mysql+pymysql://'root:12345678'@localhost:3306/shortdb > app/models.py


# dev
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/shortdb?charset=utf8')
DBSession = sessionmaker(bind=engine)


def generate_short_url(original_short):
    short_url = ShortUrl()
    pass


def get_original_url(short_url):
    short_id = utils.short_to_id(short_url)
    session = DBSession()
    short_url_po = session.query(ShortUrl).filter(ShortUrl.id == short_id).first()
    if short_url_po:
        return short_url_po.original_url
