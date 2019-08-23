from dotenv import load_dotenv
from os import getenv

load_dotenv()

dbusername = getenv("STATBUS_DBUSERNAME")
dbpassword = getenv("STATBUS_DBPASSWORD")
dbhost = getenv("STATBUS_DBHOST")
dbport = getenv("STATBUS_DBPORT")
dbname = getenv("STATBUS_DBNAME")

CACHE_TYPE = "filesystem"
CACHE_DIR = "/tmp/flask" # This needs to exist