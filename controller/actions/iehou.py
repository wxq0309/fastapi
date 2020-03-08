import orm
from fastapi import BackgroundTasks

from dao.iehou import IHou
from model.iehou import CreateIeHou
from utils.es import insert_values


async def create_ihou(info: dict):
    try:
        await IHou.objects.get(title=info['title'])
    except orm.exceptions.NoMatch as e:
        document = await IHou.objects.create(**info)
        BackgroundTasks().add_task(insert_values(document.__dict__))


async def get_alls_info():
    return await IHou.objects.all()