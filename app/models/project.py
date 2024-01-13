from app.database.sqlite import db
import sqlalchemy as sa
import sqlalchemy.orm as so


class Project(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
