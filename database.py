import os
from sqlalchemy import create_engine, text

secret = os.environ['DB_CONNECTION_URI']
engine = create_engine(secret, echo=True, future=True, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

KEYS = ['id', 'title', 'location', 'salary', 'currency', 'responsibilities', 'requirements']


def load_jobs_from_db():
	with engine.connect() as conn:
		results = conn.execute(text('select * from jobs')).all()
		return [{key:val for key, val in zip(KEYS, result)} for result in results]


def load_job_from_db(id):
	with engine.connect() as conn:
		results = conn.execute(text(f'select * from jobs where id = {id}')).all()
		if results:
			return {key:val for key, val in zip(KEYS, results[0])}
		return None


def add_application_to_db(id, data):
	with engine.connect() as conn:
		query = text(f'INSERT INTO applications(job_id, full_name, email, linkedin, education, work, resume_url) VALUES ({id}, "{data["full_name"]}", "{data["email"]}", "{data["linkedin"]}", "{data["education"]}", "{data["work"]}", "{data["resume_url"]}")')
		conn.execute(query)