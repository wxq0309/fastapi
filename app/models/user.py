import orm

from app.models.db import database, metadata


class Users(orm.Model):
    __tablename__ = "users"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    username = orm.String(max_length=50,  allow_null=True, allow_blank=True)
    email = orm.String(max_length=50, unique=True, index=True)
    password = orm.String(max_length=255)
    phone = orm.String(max_length=11, min_length=11,
                       allow_null=True, allow_blank=True)
    permission = orm.String(max_length=50, default="normal")
