"""[General Configuration Params]
"""
from os import environ, path
from dotenv import load_dotenv
import logging
from pymongo import MongoClient
from mongoengine import connect

APP_SECRET_KEY = '1234567890'

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

#configuration for the connection with MongoDB
connect('crypto', host='mongodb://localhost:27017/')

#Configuration for logger
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,format='%(asctime)s: %(levelname)s: %(message)s')

