# -*- encoding: utf-8 -*-
"""
@File    :   emails.py    
@Contact :   1053522308@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/27 10:22 下午   wuxiaoqiang      1.0         None
"""
import asyncio
from email.mime.text import MIMEText

import aiosmtplib

from app.core.celery_app import celery_app
from app.core.config import settings


async def sendemail(to_addr: str, code: str):
    title = '<html><body><h3>亲爱的<a data-auto-link="1" href="mailto:%s" target="_blank">%s</a>,您好:</h3>' % (
        to_addr, to_addr)
    body = f'<p>请点击以下链接进行激活登录 <a href="%s">http://127.0.0.1:8000/api/v1/users/activated?code={code}</a></p>'
    tail = '如果您并不是此网站用户，可能是其他用户误输入了您的邮箱地址。</body></html>'
    html = title + body + tail

    msg = MIMEText(html, 'html', 'utf-8')
    msg['From'] = settings.EMAIL_USER
    msg['To'] = to_addr
    msg['Subject'] = "欢迎注册此网站"

    try:
        async with aiosmtplib.SMTP(hostname=settings.EMAIL_HOSTNAEM, port=settings.EMAIL_PORT, use_tls=True,
                                   username=settings.EMAIL_USER, password=settings.EMAIL_PASSWORD) as smtp:
            await smtp.send_message(msg)
    except aiosmtplib.SMTPException as e:
        print(e)
        raise e


@celery_app.task(acks_late=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3})
def decoratorEmail(To: str, code: str = "123456"):
    asyncio.run(sendemail(To, code))
