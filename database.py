from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

db_connection_string = os.getenv('DB_CONNECTION_STRING')

if db_connection_string is None:
   raise ValueError("No DB_CONNECTION_STRING set for environment variable")

engine = create_engine(db_connection_string)

def load_jobs_from_db():

   with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = []
      for row in result.all():
         jobs.append(row._asdict())

      return jobs