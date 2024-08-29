import pydantic


class SchemaNote(pydantic.BaseModel):
    title: str
    body: str


class CreateNote(SchemaNote):
    ...


class GetNote(CreateNote):
    user_id: int
    note_id: int
