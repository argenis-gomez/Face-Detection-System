from fastapi import FastAPI
from routers.user import user
from routers.faces import faces
from docs import tags_metadata

app = FastAPI(
  title="FastAPI & MongoDB CRUD",
  description="This is a simple REST API using Fastapi and MongoDB",
  version="1.0",
  openapi_tags=tags_metadata
)

app.include_router(user)
app.include_router(faces)
