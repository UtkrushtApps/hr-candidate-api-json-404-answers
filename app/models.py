from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Candidate(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)

    def __repr__(self):
        return f"<Candidate id={self.id} name={self.name!r}>"
