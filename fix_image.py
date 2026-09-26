import asyncio

from database import AsyncSessionLocal
import models


async def fix_image():
    async with AsyncSessionLocal() as db:
        user = await db.get(models.User, 1)

        user.image_file = None

        await db.commit()

        print("Default image set successfully!")


asyncio.run(fix_image())