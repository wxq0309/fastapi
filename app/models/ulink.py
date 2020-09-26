import orm

from app.models.db import database, metadata


class UriLink(orm.Model):
    __tablename__ = "third_links"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    real_link = orm.String(max_length=255, allow_null=True, allow_blank=True)
    short_link = orm.String(max_length=255, allow_null=True, allow_blank=True)

    def __str__(self):
        return self.short_link
