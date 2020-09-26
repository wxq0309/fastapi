import orm

from app.models.db import database, metadata


class Spiders(orm.Model):
    __tablename__ = "spiders"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    title = orm.String(max_length=255, allow_null=True, allow_blank=True)
    publish_time = orm.String(max_length=20, allow_null=True, allow_blank=True)
    content = orm.Text(allow_null=True, allow_blank=True)
    group = orm.String(max_length=20, allow_null=True, allow_blank=True)
    is_activated = orm.Boolean(default=False)
