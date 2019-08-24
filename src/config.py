from dotenv import load_dotenv
from os import getenv

# This should always be the first line.
load_dotenv()

DB_USER = getenv("STATBUS_DBUSERNAME")
DB_PASS = getenv("STATBUS_DBPASSWORD")
DB_HOST = getenv("STATBUS_DBHOST")
DB_PORT = getenv("STATBUS_DBPORT")
DB_NAME = getenv("STATBUS_DBNAME")

CACHE_TYPE = "filesystem"
CACHE_DIR = "/tmp/flask" # This needs to exist