from dotenv import load_dotenv

load_dotenv()


def get_db_credentials():
  HOST = os.getenv('HOST')
  USER = os.getenv('USER')
  PASSWORD = os.getenv('PASSWORD')
  DB = os.getenv('DB')
  PORT = os.getenv('PORT')

  return HOST, USER, PASSWORD, DB, PORT