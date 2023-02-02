from beanie import Document, free_fall_migration


class OldModel(Document):
    name: str

    class Settings:
        name = "test_collection"


class NewModel(Document):
    name: str
    new_field: str

    class Settings:
        name = "test_collection"


class Forward:

    @free_fall_migration(document_models=[OldModel, NewModel])
    async def add_new_field(self, session):
        async for old_data in OldModel.find_all():
            new_data = NewModel(
                **old_data.dict(),
                new_field='yay'
            )
            await new_data.replace(session=session)


class Backward:
    @free_fall_migration(document_models=[OldModel, NewModel])
    async def remove_new_field(self, session):
        async for new_data in NewModel.find_all():
            new_data_dict = new_data.dict()
            new_data_dict.pop('new_field')
            old_data = OldModel(
                **new_data_dict
            )
            await old_data.replace(session=session)
