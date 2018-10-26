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
import datetime

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


def generate_short_url(original_url):
    """
    Sharding is a must if this TinyUrlService need to support high concurrency
    :param original_url: 
    :return: 
    """
    session = DBSession()
    short_url_in_db = session.query(ShortUrl).filter(ShortUrl.original_url == original_url).first()
    if short_url_in_db:
        short_id = short_url_in_db.id
        hash_str = utils.encode_base64(short_id)
        return hash_str

    short_url = ShortUrl()
    short_url.original_url = original_url
    current = datetime.datetime.now()
    short_url.createdTime = current
    short_url.updatedTime = current
    try:
        session.add(short_url)
        session.commit()
        short_id = short_url.id
        hash_str = utils.encode_base64(short_id)
        session.query(ShortUrl).filter(ShortUrl.id == short_id).update({
            "short_url": hash_str
        })
        session.commit()
        session.close()
        return hash_str
    except Exception as e:
        logging.error('ERROR generate_short_url url:%s,error:%s' % (original_url, e))


def get_original_url(short_url):
    """
    NoSQL cluster is a must if this TinyUrlService need to support high concurrency
    this can be optimized too
    :param short_url: 
    :return: 
    """
    short_id = utils.short_to_id(short_url)
    session = DBSession()
    short_url_po = session.query(ShortUrl).filter(ShortUrl.id == short_id).first()
    session.close()
    if short_url_po:
        return short_url_po.original_url
