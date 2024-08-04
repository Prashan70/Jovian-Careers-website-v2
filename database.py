from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://u1mq1qf0qiyrbddb:MkJ4q9C297Dm1yQfrF6D@baovwjcwkyn1qe5wdcgv-mysql.services.clever-cloud.com/baovwjcwkyn1qe5wdcgv?charset=utf8mb4")

def load_jobs_from_db():

   with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = [row._asdict for row in result.all()]
      return jobs