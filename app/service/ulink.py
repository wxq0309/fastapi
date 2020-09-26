from hashlib import md5

from app.models.ulink import UriLink


async def create_ulink(real_link: str):
    m5 = md5()
    m5.update(real_link.encode("utf-8"))
    return await UriLink.objects.create(real_link=real_link, short_link=m5.hexdigest()[:8])


async def get_ulink(m5: str):
    return await UriLink.objects.filter(short_link=m5).all()
