from app.database.sqlite import db
import sqlalchemy as sa
import sqlalchemy.orm as so


class Order(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
