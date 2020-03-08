import orm

from dao.db import database, metadata, DATABASE_URL


class UriLink(orm.Model):
    __tablename__ = "uri_link"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    real_link = orm.String(max_length=255, allow_null=True, allow_blank=True)
    short_link = orm.String(max_length=255, allow_null=True, allow_blank=True)

    def __str__(self):
        return self.short_link