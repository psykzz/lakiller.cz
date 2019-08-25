from dotenv import load_dotenv
import os
from os import getenv
import tempfile

# This should always be the first line.
load_dotenv()

DATABASE = {
    "engine": "playhouse.mysql_ext.MySQLConnectorDatabase",
    "name": getenv("STATBUS_DBNAME"),
    "host": getenv("STATBUS_DBHOST"),
    "port": getenv("STATBUS_DBPORT"),
    "user": getenv("STATBUS_DBUSERNAME"),
    "passwd": getenv("STATBUS_DBPASSWORD"),
}

CACHE_TYPE = "filesystem"
CACHE_DIR = tempfile.mkdtemp()