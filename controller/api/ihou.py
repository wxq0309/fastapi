from fastapi import APIRouter, BackgroundTasks, Query

from model.iehou import CreateIeHou
from controller.actions.iehou import create_ihou, get_alls_info
from utils.iehou_spider import IeHouSpider
from utils.es import match_alls, match_info, suggest_search

router = APIRouter()


@router.post("/info/")
async def info (info: CreateIeHou):
    return await create_ihou(info.dict())


@router.post("/bulk_update/")
# async def start_spider(background_task: BackgroundTasks):
async def start_spider():
    resp = IeHouSpider().get_list_info()
    for i in resp:
        await create_ihou(i)
    return {"code": 0, "msg": "正在进行获取最新数据"}


@router.get("/info/")
async def info():
    return await get_alls_info()


@router.get("/filter/")
async def es(keys: str = Query(None, alias='q')):
    return match_info(keys)

@router.get("/alls/")
async def es():
    return match_alls()


@router.get("/suggest/")
async def es(keys: str=Query(None)):
    print(keys)
    return suggest_search(keys)