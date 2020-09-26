from app.models import Users


async def create_user(user: dict):
    await Users.objects.create(**user)
