from dotenv import load_dotenv
import os
import tempfile

# This should always be the first line.
load_dotenv()

DATABASE = {
	"engine": "playhouse.mysql_ext.MySQLConnectorDatabase",
	"name": os.getenv("STATBUS_DBNAME"),
	"host": os.getenv("STATBUS_DBHOST"),
	"port": os.getenv("STATBUS_DBPORT"),
	"user": os.getenv("STATBUS_DBUSERNAME"),
	"passwd": os.getenv("STATBUS_DBPASSWORD"),
}

CACHE_TYPE = "filesystem"
CACHE_DIR = tempfile.mkdtemp()