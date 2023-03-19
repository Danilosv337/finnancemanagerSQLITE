from dotenv import load_dotenv
from os import environ
# from mysql.connector import connect
# from mysql.connector.errors import InternalError,ProgrammingError,OperationalError,DatabaseError
from sqlite3 import connect
from logging import basicConfig,FileHandler,StreamHandler, DEBUG,INFO,ERROR,CRITICAL,debug,info,error



# keys
load_dotenv('.env')

host = environ.get('host')
user = environ.get('user')
password = environ.get('password')
database = environ.get('database')

#Database
try:
    # finnance_db = connect(host=host,user=user,password=password,database=database)
    finnance_db = connect('finnance.sql')
    finnance = finnance_db.cursor()#buffered=True
except Exception:
    finnance_db = None
    finnance = None
    error('No Conection Or Database Exists')

    exit()

#Log

Azul = '\033[94m'
Fim = '\033[0m'

filelog = FileHandler("logging.log","w",delay=True)
filelog.setLevel(CRITICAL)

basicConfig(
    level=DEBUG,
    encoding="UTF-8",
    datefmt= 'Data: %d/%m/%Y  Horário: %I:%M:%S %p',
    format=f"{Azul} %(levelname)s {Fim} | %(message)s - %(asctime)s",
    handlers=[filelog,StreamHandler()]
)
