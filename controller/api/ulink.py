from fastapi import APIRouter, Query
from starlette.responses import RedirectResponse, Response

from model.ulink import CreateUriLink, UriLink
from controller.actions.ulink import create_ulink, get_ulink

router = APIRouter()


@router.post("/lts/")
async def ulink(ulink: CreateUriLink):
    slink = await create_ulink(ulink.real_link)
    return "127.0.0.1:8000/ulink/lts?url="+slink.short_link


@router.get("/lts/")
async def ulink(url: str = Query(...)):
    uri = await get_ulink(url)
    print(uri[0].real_link)
    return RedirectResponse(uri[0].real_link, status_code=302)
