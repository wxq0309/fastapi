import orm
from fastapi import BackgroundTasks

from app.models.iehou import Spiders
from app.utils.es import insert_values


async def create_ihou(info: dict):
    try:
        await Spiders.objects.get(title=info['title'])
    except orm.exceptions.NoMatch as e:
        document = await Spiders.objects.create(**info)
        BackgroundTasks().add_task(insert_values(document.__dict__))


async def get_alls_info():
    return await Spiders.objects.all()
