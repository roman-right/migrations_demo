import asyncio

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


class OldModel(Document):
    name: str

    class Settings:
        name = "test_collection"


async def main():
    cli = AsyncIOMotorClient("mongodb://beanie:beanie@localhost:27017")
    db = cli["test_migrations_1"]
    await init_beanie(db, document_models=[OldModel])

    instance1 = OldModel(name="TEST")
    await instance1.save()


asyncio.run(main())