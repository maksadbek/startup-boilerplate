from app.database.sqlite import db
import sqlalchemy as sa
import sqlalchemy.orm as so


class Item(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    active: so.Mapped[bool] = so.mapped_column(sa.Boolean(), index=True)
    price: so.Mapped[int] = so.mapped_column(sa.Integer())
    title: so.Mapped[str] = so.mapped_column(sa.String(256))
    description: so.Mapped[str] = so.mapped_column(sa.String(1000))
    type: so.Mapped[int] = so.mapped_column(sa.Integer)
