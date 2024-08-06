from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='C:\Prashant\V_S_code\Jovian-Careers-website-v2\secret.env')

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
   
def load_job_from_db(id):
   with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
      rows = result.all()
      if len(rows) == 0:
         return None
      else:
         return rows[0]._asdict()