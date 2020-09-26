from fastapi import APIRouter, Query

from app.service.iehou import create_ihou, get_alls_info
from app.schemas.iehou import CreateIeHou
from app.utils.es import match_info, match_alls, suggest_search
from app.utils.iehou_spider import IeHouSpider

router = APIRouter()


@router.post("/info/")
async def info(info: CreateIeHou):
    return await create_ihou(info.dict())


@router.post("/bulk_update/")
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
async def es(keys: str = Query(None)):
    return suggest_search(keys)
